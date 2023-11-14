# test_app.py
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_analyze_sentiment_api(client):
    response = client.post('/api/sentiment', json={'text': 'This is a positive message'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert 'recommended_actions' in data

def test_analyze_fraud_api(client):
    response = client.post('/api/fraud', json={'text': 'This is a potentially fraudulent message'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert 'recommended_actions' in data

def test_analyze_security_api(client):
    response = client.post('/api/security', json={'text': 'This is a security risk message'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert 'recommended_actions' in data

def test_analyze_compliance_and_confidentiality_api(client):
    response = client.post('/api/compliconfid', json={'text': 'This is a compliance and confidentiality risk message'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data
    assert 'recommended_actions' in data

def test_generate_reply_api(client):
    response = client.post('/api/generate_reply', json={'message': 'Hello, chatbot!'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'result' in data

# Add more tests as needed...