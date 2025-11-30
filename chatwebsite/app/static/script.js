async function refreshChat() {
    let res = await fetch("/messages");
    let messages = await res.json();

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = "";

    messages.forEach(msg => {
        let div = document.createElement("div");
        div.textContent = msg;
        chatBox.appendChild(div);
    });
}

async function sendMessage() {
    let input = document.getElementById("message-input");
    let text = input.value.trim();

    if (text === "") return;

    await fetch("/send", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: text})
    });

    input.value = "";
    refreshChat();
}

setInterval(refreshChat, 1000); // refresh every 1 sec

window.onload = () => {
    document.getElementById("send-btn").onclick = sendMessage;
    refreshChat();
};

