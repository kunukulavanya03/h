FastAPI Application
=====================

This is a simple FastAPI application.

Setup
-----

1. Install requirements: `pip install -r requirements.txt`
2. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

API Documentation
-----------------

The API documentation is available at `http://localhost:8000/docs`.

Usage Examples
--------------

### Register a new user

* `curl -X POST -H 'Content-Type: application/json' -d '{{"username": "john", "password": "password"}}' http://localhost:8000/api/auth/register`

### Login a user

* `curl -X POST -H 'Content-Type: application/json' -d '{{"username": "john", "password": "password"}}' http://localhost:8000/api/auth/login`

### Get user profile

* `curl -X GET -H 'Authorization: Bearer <token>' http://localhost:8000/api/users/profile`

### Get all users

* `curl -X GET -H 'Authorization: Bearer <token>' http://localhost:8000/api/users`

### Create a new item

* `curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Bearer <token>' -d '{{"name": "item", "description": "description"}}' http://localhost:8000/api/data`

### Get all items

* `curl -X GET -H 'Authorization: Bearer <token>' http://localhost:8000/api/data`

### Get an item by ID

* `curl -X GET -H 'Authorization: Bearer <token>' http://localhost:8000/api/data/1`

### Update an item

* `curl -X PUT -H 'Content-Type: application/json' -H 'Authorization: Bearer <token>' -d '{{"name": "updated item", "description": "updated description"}}' http://localhost:8000/api/data/1`

### Delete an item

* `curl -X DELETE -H 'Authorization: Bearer <token>' http://localhost:8000/api/data/1`