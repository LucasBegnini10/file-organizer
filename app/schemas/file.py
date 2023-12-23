from pydantic import BaseModel, EmailStr
from typing import Optional

class FileSchema(BaseModel):
    id: str
    folder_id: Optional[str] = None
    user_id: str
    name: str
    path: Optional[str] = None
    size: Optional[str] = None

class FileCreate(BaseModel):
    folder_id: Optional[str] = None
    name: str
    path: Optional[str] = None
    size: Optional[str] = None
