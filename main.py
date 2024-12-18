# imports
from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

# Create an instance of the fastAPI
app = FastAPI()

# Our database with the users

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Avuya", 
        last_name="Nditha",
        gender=Gender.male,
        roles=[Role.user, Role.admin]
    ),
    User(
        id=uuid4(), 
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

