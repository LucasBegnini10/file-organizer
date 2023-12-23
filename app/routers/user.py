from fastapi import APIRouter, Depends
from app.services.user import UserService
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.deps.db import get_db

class UserRouter:
    router = APIRouter()

    @router.post("/users/signup")
    async def create_user(user: UserCreate, db: Session = Depends(get_db)):
      return UserService.create(db, user)

        
    
        
        
