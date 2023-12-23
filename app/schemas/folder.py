from pydantic import BaseModel, EmailStr
from typing import Optional

class FolderSchema(BaseModel):
    id: str
    folder_parent_id: Optional[str] = None
    user_id: str
    name: str


class FolderCreate(BaseModel):
    name: str
    folder_parent_id: Optional[str] = None

class FolderUpdate(BaseModel):
    id: str
    name: str
    folder_parent_id: Optional[str] = None

