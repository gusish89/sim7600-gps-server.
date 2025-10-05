from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.data.decode("utf-8")
        print("Received:", data)
        return "OK", 200
    return "Hello Gustav your kinda cool!", 200


if __name__ == "__main__":
    # Force Flask to use port 8080 (or any other you want)
    app.run(host="0.0.0.0", port=8080)
