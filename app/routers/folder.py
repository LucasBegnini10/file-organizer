from fastapi import APIRouter, Depends
from app.services.folder import FolderService
from app.schemas.folder import FolderCreate, FolderUpdate
from app.schemas.user import UserSchema
from sqlalchemy.orm import Session
from app.deps.db import get_db
from typing import Annotated
from app.deps.auth import get_current_user
from typing import Optional

class FolderRouter:
    router = APIRouter()

    @router.post("/folders")
    async def create(
        folder: FolderCreate,
        current_user: Annotated[UserSchema, Depends(get_current_user)],  
        db: Session = Depends(get_db)
      ):
      return FolderService.create(db, current_user, folder)
    
    @router.put("/folders")
    async def update(
        folder: FolderUpdate,
        current_user: Annotated[UserSchema, Depends(get_current_user)],  
        db: Session = Depends(get_db)
      ):
      return FolderService.update(db, current_user, folder)
    
    @router.get("/folders")
    async def get_folders(
        current_user: Annotated[UserSchema, Depends(get_current_user)],  
        db: Session = Depends(get_db),
        folder_parent_id: Optional[str] = None
      ):
      return FolderService.get_folders(db, current_user, folder_parent_id)
  
       

        
    
        
        
