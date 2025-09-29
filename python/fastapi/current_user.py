from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from pydantic import BaseModel

# --- Database Setup (Simplified) ---
# In a real app, this would be in a separate file (e.g., database.py)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get a DB session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Authentication Setup (Simplified) ---
# In a real app, you'd have user models and JWT handling
class User(BaseModel):
    username: str
    email: str

def fake_decode_token(token: str) -> dict:
    # This is a placeholder for actual JWT decoding
    return {"sub": "dave@example.com", "username": "dave"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Dependency to get the current user from a token."""
    user_data = fake_decode_token(token)
    return User(username=user_data["username"], email=user_data["sub"])

# --- Main Application ---
app = FastAPI()

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Endpoint that depends on an authenticated user."""
    return current_user

@app.get("/items/")
async def read_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # Sub-dependency
):
    """
    Endpoint that uses two dependencies: one for the DB session and
    one for the current user. FastAPI handles the dependency graph.
    """
    # You can now use `db` to query your 