async function sendMessage() {
    const inputField = document.getElementById('user-input');
    const message = inputField.value.trim();
    if (message === "") return;

    displayMessage(message, 'user');
    inputField.value = "";

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        displayMessage(data.reply, 'bot');
    } catch (error) {
        displayMessage("Errore di connessione", 'bot');
    }
}

function displayMessage(text, sender) {
    const chatOutput = document.getElementById('chat-output');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.innerText = text;
    chatOutput.appendChild(messageDiv);
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}