# imports
import unittest
from fastapi.testclient import TestClient
from main import app, db
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

    
    # Test users route (users in db)
    def test_users_pass(self):
        response = self.client.get("/api/v1/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(db), 2)


    # Test users route (no users in db)
    def test_users_fail(self):
        # Clear the database to simulate no users
        db.clear()

        response = self.client.get("/api/v1/users")
        output = {"detail": "No users found in the database."}
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), output)

    
    # Test usesrs POST route (add user)
    def test_users_post_pass(self):
        user = {
            "id": str(UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6")),
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "gender": "male",
            "roles": ["admin"]
        }
        response = self.client.post("/api/v1/users", json=user)
        output = {"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "message": "User successfully added."}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), output)
        self.assertEqual(len(db), 3)


if __name__ == "__main__":
    unittest.main()