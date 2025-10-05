from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello from Flask!", 200

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.data.decode("utf-8")
    print("Received data:", data)
    return "Data received", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
