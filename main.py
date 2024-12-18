# imports
from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID

# Create an instance of the fastAPI
app = FastAPI()

# Our database with the users
db: List[User] = [
    User(
        id=UUID("32c229c9-27a7-4b01-8c80-4dcf4f881ec1"), 
        first_name="Avuya", 
        last_name="Nditha",
        gender=Gender.male,
        roles=[Role.user, Role.admin]
    ),
    User(
        id=UUID("73cd7b39-94dc-434b-b32c-529018cecc99"), 
        first_name="Deneline",
        middle_name="Samira", 
        last_name="Mathebula",
        gender=Gender.female,
        roles=[Role.student]
    )
]               


# Create a GET request (Home route)
@app.get("/")
async def root():
    return {"Hello": "World"}

# Create a GET request to return all the user in our db
@app.get("/api/v1/users")
async def fetch_users():
    return db;

# Create a POST request to add a user to our database
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

