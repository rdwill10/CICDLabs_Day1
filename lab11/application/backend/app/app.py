from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Capstone CI/CD!", 200

@app.get("/api/health")
def health():
    return jsonify({"status": "healthy", "version": "latest"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
