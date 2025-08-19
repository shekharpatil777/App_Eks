from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_photos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Photo).offset(skip).limit(limit).all()

def get_photo(db: Session, photo_id: int):
    return db.query(models.Photo).filter(models.Photo.id == photo_id).first()

def create_photo(db: Session, photo: schemas.PhotoCreate, image_url: str):
    db_photo = models.Photo(title=photo.title, description=photo.description, image_url=image_url)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def update_photo_likes(db: Session, photo_id: int):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if db_photo:
        db_photo.likes += 1
        db.commit()
        db.refresh(db_photo)
    return db_photo