# imports
import unittest
from fastapi.testclient import TestClient
from main import app
from uuid import UUID


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    # Test home route
    def test_roof(self):
        response = self.client.get("/")
        output = {"Hello": "World"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), output)

    
    
if __name__ == "__main__":
    unittest.main()