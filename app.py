from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE BOT OK"

@app.route("/callback", methods=["POST"])
def callback():

    body = request.json

    print("=== WEBHOOK RECEIVED ===")
    print(json.dumps(body, ensure_ascii=False, indent=2))

    return "OK"