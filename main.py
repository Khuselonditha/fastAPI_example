# imports
from fastapi import FastAPI

# Create an instance of the fastAPI
app = FastAPI()

# Create a GET request (Home route)
@app.get("/")
async def root():
    return {"Hello": "World"}