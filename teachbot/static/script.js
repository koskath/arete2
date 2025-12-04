document.addEventListener('DOMContentLoaded', () => {
    // --- Element Selectors ---
    const chatContainer = document.getElementById('chat-container');
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    // --- State ---
    const sessionId = chatContainer.dataset.sessionId;

    // --- Functions ---
    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        
        if (sender === 'user') {
            // For user messages, just set the text content directly.
            messageDiv.textContent = message;
        } else {
            // For agent messages, set the inner HTML to allow for complex content.
            messageDiv.innerHTML = message;
        }

        chatMessages.appendChild(messageDiv);
        // Scroll to the bottom to show the latest message.
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return messageDiv;
    }

    async function handleSendMessage() {
        const message = userInput.value.trim();
        if (message === '' || !sessionId) return;

        // Disable the send button to prevent multiple submissions.
        sendButton.disabled = true;
        sendButton.style.cursor = 'not-allowed';
        sendButton.style.opacity = '0.5';

        // Display the user's message and clear the input field.
        appendMessage('user', message);
        userInput.value = '';
        userInput.focus(); 

        // Create a placeholder for the agent's response with a typing indicator.
        const agentMessageDiv = appendMessage('agent', '');
        agentMessageDiv.innerHTML = '<span class="blinking-cursor"></span>';

        // Define KaTeX options once to reuse them.
        const katexOptions = {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '\\[', right: '\\]', display: true},
                {left: '$', right: '$', display: false},
                {left: '\\(', right: '\\)', display: false} // Corrected delimiters
            ],
            throwOnError: false
        };

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message, session_id: sessionId })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let fullResponseText = '';

            // Clear the blinking cursor before streaming starts.
            agentMessageDiv.innerHTML = ''; 

            // Process the streaming response from the server.
            while (true) {
                const { value, done } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value, { stream: true });
                fullResponseText += chunk;
                
                // --- Correct Rendering Order ---

                // 1. Set the raw text content first. This includes unprocessed Markdown and LaTeX.
                // Qwen
                // agentMessageDiv.textContent = fullResponseText.replace(/<\|im_end\|>/g, '');
                // llama
                agentMessageDiv.textContent = fullResponseText.replace(/<\|eot_id\|>/g, '');

                // 2. Render the math using KaTeX. This finds and converts LaTeX into HTML.
                renderMathInElement(agentMessageDiv, katexOptions);

                // 3. Parse the Markdown. It will treat the rendered math (now HTML spans) as regular HTML and ignore it.
                agentMessageDiv.innerHTML = marked.parse(agentMessageDiv.innerHTML);

                // Keep the view scrolled to the bottom as new content streams in.
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        } catch (error) {
            console.error('Error sending message:', error);
            agentMessageDiv.textContent = 'Sorry, I encountered an error. Please try again.';
        } finally {
            // Re-enable the send button after the response is complete or an error occurs.
            sendButton.disabled = false;
            sendButton.style.cursor = 'pointer';
            sendButton.style.opacity = '1';
            // Ensure the blinking cursor is removed.
            agentMessageDiv.querySelector('.blinking-cursor')?.remove();
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }

    // --- Event Listeners ---
    sendButton.addEventListener('click', handleSendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !sendButton.disabled) {
            handleSendMessage();
        }
    });

    // --- Initial Setup ---
    appendMessage('agent', 'Ask me anything related to Linear Algebra.');
    userInput.focus();
});