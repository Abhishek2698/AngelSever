from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the latest received token in memory
latest_token = {}

@app.route("/")
def index():
    return "Angel One Callback Server is running", 200

@app.route("/callback")
def callback():
    code = request.args.get("code", "")
    auth_token = request.args.get("auth_token", "")

    # Angel One may send either 'code' or 'auth_token'
    token = code or auth_token

    if token:
        latest_token["value"] = token
        print(f"[CALLBACK] Received token: {token}")
        return "Auth token received successfully. You can close this window.", 200
    else:
        return "No token received in callback.", 400

@app.route("/token")
def get_token():
    """Fetch the latest received token programmatically"""
    if latest_token.get("value"):
        return jsonify({"token": latest_token["value"]}), 200
    return jsonify({"error": "No token received yet"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
