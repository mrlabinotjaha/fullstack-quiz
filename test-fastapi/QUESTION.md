# FastAPI Quiz - User CRUD API

## Overview

Build a simple REST API using **FastAPI** that manages users in an in-memory list. You will work in `main.py` where TODOs guide you through each step.

### 1. Endpoints

| Method | Path            | Status Code | Description                          |
|--------|-----------------|-------------|--------------------------------------|
| POST   | `/users`        | 201         | Create a new user                    |
| GET    | `/users`        | 200         | Get all users                        |
| GET    | `/users/{user_id}` | 200      | Get a user by ID (404 if not found)  |

- The POST endpoint should assign an `id` as `len(db) + 1`, append the user to the db, and return it
- The GET by ID endpoint should raise `HTTPException(status_code=404)` if the user is not found
- All endpoints should use `Depends(get_users_db)` to access the database

## How to Run

```bash
cd test-fastapi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run tests
```bash
make test
```

All 8 tests must pass.

## Evaluation Criteria

- Correct use of FastAPI decorators and status codes
- Proper Pydantic model validation with field constraints
- Correct use of dependency injection with `Depends`
- Proper error handling with `HTTPException`
