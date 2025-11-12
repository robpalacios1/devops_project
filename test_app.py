# test_app.py
"""Unit tests for the Flask API endpoints."""
import json
from app import app

def test_home():
    """Test that the main route '/' works and returns the correct JSON."""
    client = app.test_client()
    response = client.get('/')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["message"] == "Test Of Deployment! This is my DevOps Project."

def test_status():
    """Test that the status route '/status' works and returns 'ok'."""
    client = app.test_client()
    response = client.get('/status')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["status"] == "ok"
