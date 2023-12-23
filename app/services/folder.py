from app.repositories.folder import FolderRepository
from sqlalchemy.orm import Session
from app.schemas.folder import FolderUpdate, FolderCreate
from app.schemas.user import UserSchema

class FolderService:
  def create(db: Session, current_user: UserSchema, folder: FolderCreate):
    return FolderRepository.create(db, current_user.id, folder)
  
  def update(db: Session, current_user: UserSchema, folder: FolderUpdate):
    return FolderRepository.update(db, folder)
  
  def get_folders(db: Session, current_user: UserSchema, folder_parent_id: str = None):
    return FolderRepository.get_folders(db, current_user.id, folder_parent_id)
  

    
        