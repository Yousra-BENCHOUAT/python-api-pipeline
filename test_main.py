from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()["items"]) == 3

def test_get_item_exists():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_item_not_found():
    response = client.get("/items/99")
    assert response.status_code == 200
    assert response.json()["error"] == "item not found"