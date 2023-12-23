from app.repositories.user import UserRepository
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.user import UserCreate

class UserService:
    def get_user_by_email(db: Session, email: str):
        return UserRepository.get_user_by_email(db, email)
    
    def create(db: Session, user: UserCreate):
        try: 
            user_created = UserRepository.create(db, user)
            del user_created.password
            return user_created
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        