import subprocess
import sys
import time

import pytest
import requests

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope="module", autouse=True)
def flask_server():
    process = subprocess.Popen([sys.executable, "app.py"])
    for _ in range(20):
        try:
            requests.get(f"{BASE_URL}/health", timeout=0.5)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    yield
    process.terminate()
    process.wait()


def test_app_is_available():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_items_endpoint():
    response = requests.get(f"{BASE_URL}/items")
    assert response.status_code == 200
    assert "premier item" in response.json()["items"]
