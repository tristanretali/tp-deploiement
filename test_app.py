from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_items():
    client = app.test_client()
    response = client.get("/items")
    assert response.status_code == 200
    assert response.get_json() == {"items": ["premier item", "deuxieme item"]}
