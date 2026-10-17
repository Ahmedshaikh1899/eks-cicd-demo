from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Production EKS Pipeline with Security Scans!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
