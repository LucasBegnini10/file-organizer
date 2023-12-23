from sqlalchemy import Column, String, ForeignKey, DateTime
from app.config.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class FileModel(Base):
    __tablename__ = "files"
    
    id = Column(String(36), primary_key=True, index=True)
    folder_id = Column(String(36), ForeignKey("folders.id"))
    user_id = Column(String(36), ForeignKey("users.id"))
    name = Column(String(1024))
    path = Column(String(512))
    size = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    folder = relationship("FolderModel", back_populates="files")