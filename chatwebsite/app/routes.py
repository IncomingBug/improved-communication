from flask import Blueprint, render_template, request, jsonify

main = Blueprint("main", __name__)

messages = []   # super-simple storage in RAM

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/chat")
def chat():
    return render_template("chat.html")

@main.route("/send", methods=["POST"])
def send():
    data = request.json
    message = data.get("message", "")

    if message.strip():
        messages.append(message)

    return jsonify({"status": "ok"})

@main.route("/messages")
def get_messages():
    return jsonify(messages)
