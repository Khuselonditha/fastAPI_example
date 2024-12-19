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


    # Test users POST route (user already exists)
    def test_users_post_fail(self):
        user = {
            "id": str(UUID("32c229c9-27a7-4b01-8c80-4dcf4f881ec1")),
            "first_name": "Khuselo",
            "middle_name": "Lolo",
            "last_name": "Nditha",
            "gender": "male",
            "roles": ["admin"]
        }
        response = self.client.post("/api/v1/users", json=user)
        output = {"detail": "User with id: 32c229c9-27a7-4b01-8c80-4dcf4f881ec1 already exists."}
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), output)
        self.assertEqual(len(db), 2)
        

    # Test users DELETE route (remove user in db)
    def test_users_delete_pass(self):
        user_id = "32c229c9-27a7-4b01-8c80-4dcf4f881ec1"
        response = self.client.delete(f"/api/v1/users/{user_id}")
        output = {"id": "32c229c9-27a7-4b01-8c80-4dcf4f881ec1", "message": "User successfully removed."}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), output)
        self.assertEqual(len(db), 1)

    # Test users DELETE route (user not in db)
    def test_users_delete_fail(self):
        user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        response = self.client.delete(f"/api/v1/users/{user_id}")
        output = {"detail": "User with id: 3fa85f64-5717-4562-b3fc-2c963f66afa6 does not exist."}
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), output)
        self.assertEqual(len(db), 2)


if __name__ == "__main__":
    unittest.main()