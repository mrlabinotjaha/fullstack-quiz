# TODO: Import FastAPI, Depends, HTTPException from fastapi
# TODO: Import BaseModel, Field from pydantic
# TODO: Import List from typing

app = FastAPI()

users_db = []

# ──────────────────────────────────────────────
# Pydantic Models
# ──────────────────────────────────────────────

class UserCreate(BaseModel):
    # TODO: Define fields: name (str, min 3), email (str, min 5), is_active (bool, default True)
    pass


class User(UserCreate):
    # TODO: Add an id: int field
    pass


# ──────────────────────────────────────────────
# Dependencies
# ──────────────────────────────────────────────

def get_users_db():
    # TODO: Return the in-memory users_db list
    pass


# ──────────────────────────────────────────────
# Endpoints
# ──────────────────────────────────────────────

# TODO: Create a POST /users endpoint (status_code 201, response_model User)
def create_user():
    pass


# TODO: Create a GET /users endpoint (response_model List[User])
def get_users():
    pass


# TODO: Create a GET /users/{user_id} endpoint (response_model User, raise 404 if not found)
def get_user():
    pass
