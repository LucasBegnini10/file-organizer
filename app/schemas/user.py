from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    document: str
    phone: Optional[str] = None
    password: str
    is_active: bool

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    document: str
    phone: Optional[str] = None
    password: str

class UserLoginSchema(BaseModel):    
    email: EmailStr
    password: str
