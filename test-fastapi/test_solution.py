from fastapi.testclient import TestClient
from main import app, users_db


client = TestClient(app)


def setup_function():
    users_db.clear()


def test_create_user():
    resp = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert data["is_active"] is True


def test_create_user_default_is_active():
    resp = client.post("/users", json={"name": "Bob", "email": "bob@example.com", "is_active": False})
    assert resp.status_code == 201
    assert resp.json()["is_active"] is False


def test_create_user_name_too_short():
    resp = client.post("/users", json={"name": "Al", "email": "al@example.com"})
    assert resp.status_code == 422


def test_create_user_email_too_short():
    resp = client.post("/users", json={"name": "Alice", "email": "a@b"})
    assert resp.status_code == 422


def test_get_users_empty():
    resp = client.get("/users")
    assert resp.status_code == 200
    assert resp.json() == []


def test_get_users_after_create():
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    client.post("/users", json={"name": "Bobby", "email": "bob@example.com"})
    resp = client.get("/users")
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_get_user_by_id():
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Alice"


def test_get_user_not_found():
    resp = client.get("/users/999")
    assert resp.status_code == 404
