from flask import Flask, request

app = Flask(__name__)

# Store the latest GPS data
latest_data = "No data yet"

@app.route("/", methods=["GET"])
def home():
    return f"Latest GPS data: {latest_data}", 200

@app.route("/data", methods=["POST"])
def receive_data():
    global latest_data
    latest_data = request.data.decode("utf-8")  # Update latest GPS data
    print("Received data:", latest_data)        # Still prints to logs
    return "Data received", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
