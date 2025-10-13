from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "latest_data.txt"

@app.route("/", methods=["GET"])
def home():
    """Display the latest data sent to the server."""
    try:
        with open(DATA_FILE, "r") as f:
            latest_data = f.read()
    except FileNotFoundError:
        latest_data = "No data yet"
    return f"Latest data:<br>{latest_data}", 200

@app.route("/data", methods=["POST"])
def receive_data():
    """Receive any text via POST and save it."""
    text = request.form.get("text")  # get the "text" field

    if not text:
        return "No text received", 400

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    data = f"{timestamp} → {text}"

    # Save to file
    with open(DATA_FILE, "w") as f:
        f.write(data)

    print("Received data:", data)
    return "Data received", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

