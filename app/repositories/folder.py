from app.models.folder import FolderModel
from sqlalchemy.orm import Session
from app.schemas.folder import FolderCreate, FolderUpdate
from app.utils.uuid import generate
from app.repositories.file import FileRepository 

class FolderRepository:  
  def create(db: Session, user_id: str, folder: FolderCreate):
    db_folder = FolderModel(
      id=generate(),
      folder_parent_id=folder.folder_parent_id,
      user_id=user_id,
      name=folder.name
    )
    
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder
  
  def update(db: Session, folder: FolderUpdate):
    print(folder)
    folder_found = FolderRepository.get_by_id(db, folder.id)

    folder_found.name = folder.name
    folder_found.folder_parent_id = folder.folder_parent_id

    db.add(folder_found)
    db.commit()
    db.refresh(folder_found)
    return folder_found

  def get_by_id(db: Session, id: str):
    return db.query(FolderModel).filter(FolderModel.id == id).first()
  
  def get_folders(db: Session, user_id: str, folder_parent_id: str = None):
    folders = db.query(FolderModel).filter_by(user_id=user_id, folder_parent_id=folder_parent_id).all()
    files = FileRepository.get_files_without_folder(db, user_id)

    return {"folders": folders, "files": files}


    

  

