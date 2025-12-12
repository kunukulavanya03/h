# h Backend API

## Overview

This is a FastAPI backend API for the h frontend application.

## Requirements

* Python 3.9+
* FastAPI 0.104.1+
* SQLAlchemy 2.0.0+
* python-dotenv 0.19.0+
* python-jose 3.3.0+
* passlib 1.7.4+
* bcrypt 4.0.0+

## Setup

1. Create a new virtual environment: `python -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Create a new database: `sqlite3 app.db`
5. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Documentation

The API documentation can be found at <http://localhost:8000/docs>.

## Usage

To use the API, send a request to the desired endpoint with the required parameters.

For example, to register a new user, send a POST request to <http://localhost:8000/api/auth/register> with the following JSON body:

```
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "password123"
}
```

This will return a JSON response with the user's token and profile information.

## API Endpoints

* **GET /api/health**: Health check endpoint
* **POST /api/auth/login**: User authentication
* **POST /api/auth/register**: User registration
* **GET /api/users**: Get all users
* **GET /api/users/{id}**: Get user by ID
* **POST /api/items**: Create new item
* **GET /api/items**: Get all items
* **PUT /api/items/{id}**: Update item by ID
* **DELETE /api/items/{id}**: Delete item by ID