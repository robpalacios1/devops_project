# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Main route that returns a greeting."""
    return jsonify({"message": "Test Of Deployment! This is my DevOps Project."})

@app.route('/status')
def status():
    """Health check route to check if the app is alive."""
    return jsonify({"status": "ok", "service": "my-api-devops"})

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)