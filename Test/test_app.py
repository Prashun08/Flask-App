import pytest
from unittest.mock import patch
from app import app
import mongomock

@pytest.fixture
def client():
    app.config['TESTING'] = True
    mock_db = mongomock.MongoClient().db
    with patch('app.get_db', return_value=(mock_db, mock_db.collection)):
        with app.test_client() as client:
            yield client

def test_add(client):
    response = client.post('/add', json={"x": 10, "y": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert "Value" in data
    assert data["Value"] == 15

def test_subtract(client):
    response = client.post('/subtract', json={"x": 10, "y": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert "Value" in data
    assert data["Value"] == 5

def test_multiply(client):
    response = client.post('/multiply', json={"x": 10, "y": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert "Value" in data
    assert data["Value"] == 50

def test_divide(client):
    response = client.post('/divide', json={"x": 10, "y": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert "Value" in data
    assert data["Value"] == 2

def test_missing_x(client):
    response = client.post('/add', json={"y": 5})
    assert response.status_code == 301

def test_missing_y(client):
    response = client.post('/subtract', json={"x": 10})
    assert response.status_code == 302

def test_divide_by_zero(client):
    response = client.post('/divide', json={"x": 10, "y": 0})
    assert response.status_code == 303
