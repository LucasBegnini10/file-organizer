from app.models.file import FileModel
from sqlalchemy.orm import Session
from app.schemas.file import FileCreate
from app.utils.uuid import generate

class FileRepository:  
  def create(db: Session, user_id: str, file: FileCreate):
    db_file = FileModel(
      id=generate(),
      folder_id = file.folder_id,
      user_id =  user_id,
      name = file.name,
      path = file.path,
      size = file.size,
    )
    
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

  def get_by_id(db: Session, id: str):
    return db.query(FileModel).filter(FileModel.id == id).first()
  
  def get_files_without_folder(db: Session, user_id: str):
    return db.query(FileModel).filter(FileModel.user_id == user_id and FileModel.folder_id == None).all()

    

  

