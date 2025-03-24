# User Management API

This project is a simple User Management API built with FastAPI. The API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on a user database.

## Features

* **Get All Users**: Retrieve all users in the database.

* **Add a User**: Add a new user to the database.

* **Update User Information**: Update the details of an existing user.

* **Delete a User**: Remove a user from the database.

## Prerequisites

* Python 3.8+

* FastAPI

* Uvicorn[standard] (for running the server)

## Installation

1. Clone the repository:
``` bash
git clone git@github.com:Khuselonditha/fastAPI_example.git
cd fastAPI_example
```

2. Create a virtual environment:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the dependencies:
``` bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server with Uvicorn:
``` bash
python3 -m uvicorn main:app --reload
```

2. Access the API documentation in your browser:
    * Swagger UI: http://127.0.0.1:8000/docs
    * ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Home
``` python
GET /

Returns a simple greeting message.

Response:

{
    "Hello": "World"
}
```

### Get All Users
``` python
GET /api/v1/users

Retrieves all users in the database.

Response:

[
    {
        "id": "<UUID>",
        "first_name": "<First Name>",
        "last_name": "<Last Name>",
        "gender": "<Gender>",
        "roles": ["<Role1>", "<Role2>"]
    }
]
```
### Add a User
``` python
POST /api/v1/users

Adds a new user to the database.

Request Body:

{
    "first_name": "<First Name>",
    "middle_name": "<Middle Name>",
    "last_name": "<Last Name>",
    "gender": "<Gender>",
    "roles": ["<Role1>", "<Role2>"]
}
```
``` python
Response:

{
    "id": "<UUID>",
    "message": "User successfully added."
}
```
### Update a User
``` python
PUT /api/v1/users/{user_id}

Updates an existing user's details.

Path Parameter: user_id (UUID of the user)

Request Body:

{
    "first_name": "<First Name>",
    "middle_name": "<Middle Name>",
    "last_name": "<Last Name>",
    "roles": ["<Role1>", "<Role2>"]
}
```
``` python
Response:

"Information updated successfully."
```
### Delete a User
``` python
DELETE /api/v1/users/{user_id}

Deletes a user from the database.

Path Parameter: user_id (UUID of the user)

Response:

"User successfully removed."
```
## Models

### User Model

* **id**: UUID (auto-generated if not provided)

* **first_name**: string

* **middle_name**: string (optional)

* **last_name**: string

* **gender**: Enum ("male", "female")

* **roles**: List of Enum ("admin", "user", "student")

## User Update Request Model

* **first_name**: string (optional)

* **middle_name**: string (optional)

* **last_name**: string (optional)

* **roles**: List of Enum (optional)

## Error Handling

The API returns appropriate error messages with HTTP status codes in case of invalid requests or operations:

* **400 Bad Request**: When trying to add a user with an already existing ID.

* **404 Not Found**: When a resource (user) is not found.

## License

This project is licensed under the MIT License.

## Acknowledgments

Built using FastAPI.

Inspired by the simplicity and performance of modern Python frameworks.