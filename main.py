# imports
from fastapi import FastAPI

# Create an instance of the fastAPI
app = FastAPI()

# Create a GET request (Home route)
@app.get("/")
def root():
    return {"Hello": "World"}