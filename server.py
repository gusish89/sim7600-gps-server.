from flask import Flask, request
from datetime import datetime


app = Flask(__name__)


DATA_FILE = "latest_gps.txt"


@app.route("/", methods=["GET"])
def home():
    """Display the latest data."""
    try:
        with open(DATA_FILE, "r") as f:
            latest_data = f.read()
    except FileNotFoundError:
        latest_data = "No data yet"
    return f"Latest data:<br>{latest_data}", 200


@app.route("/data", methods=["POST"])
def receive_data():
    """Receive any POST data and save/display it."""
    # Get all form data (key=value) as a dict
    form_data = request.form.to_dict()
    
    # If JSON is sent instead of form, you can also handle it:
    if not form_data and request.is_json:
        form_data = request.get_json()


    # Convert to string
    data_str = str(form_data) if form_data else "No data received"


    # Add timestamp
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    final_data = f"{timestamp} → {data_str}"


    # Save to file
    with open(DATA_FILE, "w") as f:
        f.write(final_data)


    # Print to server logs
    print("Received data:", final_data)


    return "Data received", 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)



