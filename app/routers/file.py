from fastapi import APIRouter, UploadFile, Depends
from typing import Annotated
from app.deps.auth import get_current_user
from app.schemas.user import UserSchema
from app.services.file import FileService
from app.deps.db import get_db
from sqlalchemy.orm import Session

class FileRouter:
    router = APIRouter()

    @router.post("/files")
    async def create(
        file: UploadFile,
        current_user: Annotated[UserSchema, Depends(get_current_user)],
        db: Session = Depends(get_db),
        folder_id: str = None
    ):
        return FileService.create(db, current_user, file, folder_id)
        
        
        
        
