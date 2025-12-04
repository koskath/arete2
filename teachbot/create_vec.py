import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.schema import Document
import glob

device = "mps"
model_name = "Qwen/Qwen3-Embedding-0.6B"
db_name = "ml_vstore"

embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"device": "mps"})

folders = glob.glob("ML")
text_loader_kwargs = {'encoding': 'utf-8'}

documents = []
for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        documents.append(doc)


vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=db_name)
print(f"Vectorstore created with {vectorstore._collection.count()} documents")
