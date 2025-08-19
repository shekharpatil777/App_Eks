from pydantic import BaseModel, HttpUrl
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    is_admin: bool = False

class UserInDB(UserBase):
    id: int
    hashed_password: str
    is_admin: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Photo Schemas
class PhotoBase(BaseModel):
    title: str
    description: Optional[str] = None

class PhotoCreate(PhotoBase):
    pass # Image will be uploaded separately

class PhotoUpdate(PhotoBase):
    image_url: Optional[HttpUrl] = None
    likes: Optional[int] = None

class Photo(PhotoBase):
    id: int
    image_url: HttpUrl
    likes: int

    class Config:
        orm_mode = True