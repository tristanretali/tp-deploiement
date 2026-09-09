import subprocess
import sys
import time
import unittest

import requests

BASE_URL = "http://127.0.0.1:8080"


class AppE2ETestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.process = subprocess.Popen([sys.executable, "app.py"])
        for _ in range(20):
            try:
                requests.get(f"{BASE_URL}/health", timeout=0.5)
                break
            except requests.exceptions.ConnectionError:
                time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
        cls.process.wait()

    def test_app_is_available(self):
        response = requests.get(f"{BASE_URL}/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_items_endpoint(self):
        response = requests.get(f"{BASE_URL}/items")
        self.assertEqual(response.status_code, 200)
        self.assertIn("premier item", response.json()["items"])


if __name__ == "__main__":
    unittest.main()
