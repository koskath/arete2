from flask import Flask, render_template, request, jsonify, session, Response, stream_with_context
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import torch
import uuid
import threading
import queue
import secrets
import string
import warnings
from huggingface_hub import login
from dotenv import load_dotenv
from mysql.connector import pooling, Error as MySQLError


warnings.filterwarnings("ignore")
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
session_histories = {}
session_lock = threading.Lock()
tokenizer = None
model_name = "../models/llama-3b-mini-training-theory/llama-3b-mini-training-theory-teachbot"
device = "cuda"
embeddings_model_name = "qwen_embeddings"
db_name = "linear_algebra_vstore"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name, model_kwargs={"device": device})
vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)

load_dotenv()

def make_pool():
    return pooling.MySQLConnectionPool(
        pool_name="teachbot_pool",
        pool_size=5,                 # adjust if you have more concurrency
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "teachbot"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DB", "teachbot_cbs"),
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci",
    )
def log_turn_to_db(session_id: str, question: str, response: str):
    try:
        conn = db_pool.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO chat_history (session_id, question, response) VALUES (%s, %s, %s)",
                (session_id, question, response),
            )
    except MySQLError as e:
        # Don’t crash the request if logging fails—just print a warning.
        print(f"[DB] Insert failed: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            pass

db_pool = make_pool()


HIGH_SCORE_THRESHOLD = 0.5
MEDIUM_SCORE_THRESHOLD = 0.4
LOW_SCORE_THRESHOLD = 0.3

def retrieve_relevant_context(message, k=25):
    hits = vectorstore.similarity_search_with_relevance_scores(message, k=k)
    high, med, low = [], [], []
    for doc, sim in hits:
        content = doc.page_content
        if sim >= HIGH_SCORE_THRESHOLD:
            high.append(content)
        elif sim >= MEDIUM_SCORE_THRESHOLD:
            med.append(content)
        elif sim >= LOW_SCORE_THRESHOLD:
            low.append(content)

    final_docs = []
    if high:
        final_docs.extend(high[:5])
        if len(final_docs) < 5 and med:
            need = 5 - len(final_docs)
            final_docs.extend(med[:need])
    else:
        if med:
            take = min(3, len(med))
            final_docs.extend(med[:take])
            if take < 3:
                if low:
                    final_docs.append(low[0])
                else:
                    return message
        else:
            if low:
                final_docs.append(low[0])
            else:
                return message
    if final_docs:
        relevant_context = "\n\n".join(final_docs)
        relevant_context += f"\n\nUser's Question: {message}"
        return relevant_context
    else:
        return message

class QueueStreamer(TextStreamer):
    def __init__(self, q, tokenizer, skip_prompt=True, **kwargs):
        super().__init__(tokenizer, skip_prompt=skip_prompt, **kwargs)
        self.q = q
        self.eos_token = tokenizer.eos_token

    def on_finalized_text(self, text: str, stream_end: bool = False):
        if text == self.eos_token:
            self.q.put(None)
            return
        self.q.put(text)
        if stream_end:
            self.q.put(None)

def load_model_and_tokenizer(model_name = model_name):
    """Loads the model and tokenizer."""
    global tokenizer, model, device
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("Using cuda device.")
    else:
        device = torch.device("cpu")
        print("Falling back to CPU.")

    print(f"Loading model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, local_files_only=True)
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    # model = AutoModelForCausalLM.from_pretrained(model_name)
    try:
        model = torch.compile(model, 
                            #   mode="reduce-overhead"
                            backend="aot_eager")
        print("Model compiled successfully.")
    except Exception as e:
        print(f"torch.compile failed: {e}. Running unoptimized.")
    model.to(device)
    print("Model and tokenizer loaded.")


system_message = "You are a friendly and supportive teaching assistant for Linear Algebra and Statistics at Copenhagen Business School."
system_message += "You answer student questions about Linear Algebra, statistics and Data Science."
system_message += "You also answer to questions about the Administration of the class.Do not answer questions about unrelated topics."
system_message += "You Provide guidance through brief, concise answers with clear steps."
system_message += "You must not give direct answers, as this upholds academic honesty."
system_message += "Your goal is to encourage the student to think critically."


with app.app_context():
    load_model_and_tokenizer()

@app.route('/')
def index():
    """Renders the main chat interface and creates a new session ID."""
    # Generate a unique ID for this user's session
    session_id = str(uuid.uuid4())
    global system_message
    # Safely create a new history for this session ID
    with session_lock:
        if session_id not in session_histories:
            session_histories[session_id] = [
                {"role": "system", "content": system_message},
            ]
            
    # Pass the session_id to the template, so the client can use it
    return render_template('index.html', session_id=session_id)

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat messages using server-side state."""
    data = request.json
    user_message = data.get('message')
    session_id = data.get('session_id') # Client must send this back

    if not all([user_message, session_id]):
        return jsonify({"error": "Message or session_id missing."}), 400

    # Retrieve and update history safely
    with session_lock:
        if session_id not in session_histories:
            # This is a fallback in case the session expired on the server
            session_histories[session_id] = [{"role": "system", "content": system_message}]
        
        # Get a reference to the specific history for this session
        conversation_history = session_histories[session_id]
        retrieved_message = retrieve_relevant_context(user_message)
        # print(user_message)
        # conversation_history.append({"role": "user", "content": retrieved_message})
        temp_history = conversation_history + [{"role": "user", "content": retrieved_message}]


    text = tokenizer.apply_chat_template(
        # conversation_history,
        temp_history,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    def generate_and_stream():
        q = queue.Queue()
        streamer = QueueStreamer(q, tokenizer, skip_prompt=True)
        
        generation_kwargs = dict(
            **model_inputs,
            streamer=streamer,
            max_new_tokens=600,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            # eos_token_id=tokenizer.eos_token_id, # nvidia ace math specific
            # pad_token_id=tokenizer.pad_token_id, # nvidia ace math specific
            pad_token_id=tokenizer.eos_token_id # It works for qwen and llama without the 2 above lines
        )

        thread = threading.Thread(target=model.generate, kwargs=generation_kwargs)
        thread.start()

        full_response = []
        while True:
            token = q.get()
            if token is None:
                break
            full_response.append(token)
            yield token

        thread.join()

        # THIS IS THE KEY FIX:
        # Update the server-side dictionary, which is safe to do from a thread.
        agent_response = "".join(full_response)
        with session_lock:
            # Ensure we're appending to the correct, latest history
            session_histories[session_id].append({"role": "user", "content": user_message})
            session_histories[session_id].append({"role": "assistant", "content": agent_response.strip()})
        log_turn_to_db(session_id=session_id, question=user_message, response=agent_response.strip())

    return Response(stream_with_context(generate_and_stream()), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True, use_reloader=False)