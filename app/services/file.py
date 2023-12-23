from fastapi import UploadFile
from app.config.s3 import s3
from app.schemas.user import UserSchema
from app.schemas.file import FileCreate
from app.repositories.file import FileRepository
from sqlalchemy.orm import Session
import os

bucket_name = os.getenv("BUCKET_NAME")

class FileService: 
  def create(db: Session, current_user: UserSchema, upload_file: UploadFile, folder_id: str = None):
    path = FileService.upload_file(upload_file, current_user)
    file = FileCreate(folder_id=folder_id, name=upload_file.filename, path=path, size=str(upload_file.size))
    return FileRepository.create(db, current_user.id, file)

  def upload_file(file: UploadFile, current_user: UserSchema):
      path = f"{current_user.id}/{file.filename}"
      s3.upload_fileobj(file.file, bucket_name, path)

      url = f"https://{bucket_name}.s3.amazonaws.com/{path}"
      return url
