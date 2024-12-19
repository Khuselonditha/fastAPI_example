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

    
    # Test users route
    def test_users_pass(self):
        response = self.client.get("/api/v1/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    

if __name__ == "__main__":
    unittest.main()