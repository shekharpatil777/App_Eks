from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import os
import shutil
from typing import List, Optional

from . import models, schemas, crud
from .database import engine, get_db
from .auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, get_current_admin_user

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000", # React frontend default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Authentication Endpoints ---

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=None # Token expires in 15 min by default
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=schemas.UserInDB)
async def read_users_me(current_user: schemas.UserInDB = Depends(get_current_user)):
    return current_user

# --- Photo Endpoints ---

@app.get("/photos/", response_model=List[schemas.Photo])
def read_photos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    photos = crud.get_photos(db, skip=skip, limit=limit)
    return photos

@app.post("/photos/", response_model=schemas.Photo)
async def create_upload_photo(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: schemas.UserInDB = Depends(get_current_admin_user) # Only admin can create
):
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)
    file_location = os.path.join(upload_folder, file.filename)
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # In a real app, you'd store this in a cloud storage (S3, GCS) and save the URL
    image_url = f"/static/{file.filename}" 
    
    photo_data = schemas.PhotoCreate(title=title, description=description)
    return crud.create_photo(db, photo_data, image_url)

@app.post("/photos/{photo_id}/like", response_model=schemas.Photo)
def like_photo(photo_id: int, db: Session = Depends(get_db)):
    photo = crud.update_photo_likes(db, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo

# Serve static files (for uploaded images)
@app.get("/static/{filename}")
async def serve_static(filename: str):
    # In a real app, this should be handled by a web server (Nginx/Apache) or cloud storage
    # For simplicity, we'll serve directly from FastAPI for local development
    from fastapi.responses import FileResponse
    file_path = os.path.join("uploads", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="File not found")