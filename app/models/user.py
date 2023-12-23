from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from app.config.db import Base
from datetime import datetime

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, index=True)
    email = Column(String(256), unique=True, index=True)
    name = Column(String(256))
    document = Column(String(14), unique=True)
    phone = Column(String(11))
    password = Column(String(500))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    folders = relationship("FolderModel", back_populates="user")
