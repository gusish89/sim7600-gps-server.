from flask import Flask, request

app = Flask(__name__)

DATA_FILE = "latest_gps.txt"

@app.route("/", methods=["GET"])
def home():
    try:
        with open(DATA_FILE, "r") as f:
            latest_data = f.read()
    except FileNotFoundError:
        latest_data = "No data yet"
    return f"Latest GPS data: {latest_data}", 200

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.data.decode("utf-8")
    with open(DATA_FILE, "w") as f:
        f.write(data)
    print("Received data:", data)  # This still goes to the logs
    return "Data received", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
