from sqlalchemy import Column, String, ForeignKey, DateTime
from app.config.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class FolderModel(Base):
    __tablename__ = "folders"
    
    id = Column(String(36), primary_key=True, index=True)
    folder_parent_id = Column(String(36), ForeignKey("folders.id"))
    user_id = Column(String(36), ForeignKey("users.id"))
    name = Column(String(1024))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("UserModel", back_populates="folders")
    files = relationship("FileModel", back_populates="folder")

    children = relationship("FolderModel", remote_side=[id])
