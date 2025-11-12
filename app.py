# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Ruta principal que devuelve un saludo."""
    return jsonify({"message": "Test Of Deployment! This is my DevOps Project."})

@app.route('/status')
def status():
    """Ruta de 'health check' para saber si la app está viva."""
    return jsonify({"status": "ok", "service": "my-api-devops"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)