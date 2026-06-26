from flask import Flask, render_template, request, jsonify
import requests
chat_history = []
app = Flask(__name__)


OLLAMA_URL = "http://localhost:11434/api/chat"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    prompt = request.json.get("prompt")
    model = request.json.get("model")
    chat_history.append({
    "role": "user",
    "content": prompt
    })

    data = {
        "model": model,
        "messages": chat_history,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=data)

    answer = response.json()["message"]["content"]

    chat_history.append({
    "role": "assistant",
    "content": answer
    })

    return jsonify({"response": answer+prompt+model})

@app.route("/models")
def models():

    r = requests.get("http://localhost:11434/api/tags")

    return r.json()

if __name__ == "__main__":
    app.run()