from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Server is running", 200

@app.route("/callback")
def callback():
    code = request.args.get("code", "")
    return f"Received code: {code}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
