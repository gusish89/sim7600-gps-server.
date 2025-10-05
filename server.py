from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "latest_gps.txt"

@app.route("/", methods=["GET"])
def home():
    """Display the latest GPS data."""
    try:
        with open(DATA_FILE, "r") as f:
            latest_data = f.read()
    except FileNotFoundError:
        latest_data = "No data yet"
    return f"Latest GPS data:<br>{latest_data}", 200

@app.route("/data", methods=["POST"])
def receive_data():
    """Receive GPS coordinates and a message via POST and save them."""
    latitude = request.form.get("Latitude")
    longitude = request.form.get("Longitude")
    message = request.form.get("Message", "")  # Optional field

    if not latitude or not longitude:
        return "Missing Latitude or Longitude", 400

    # Add timestamp for tracking
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    data = f"{timestamp} → Latitude={latitude}, Longitude={longitude}, Message={message}"

    # Save to file
    with open(DATA_FILE, "w") as f:
        f.write(data)

    # Also print to server logs
    print("Received data:", data)

    return "Data received", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

