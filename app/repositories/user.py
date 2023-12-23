from app.models.user import UserModel
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.utils.auth import AuthUtil
from app.utils.uuid import generate


class UserRepository:
  def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()
  
  def create(db: Session, user: UserCreate):
      password = AuthUtil.get_password_hash(user.password) 

      db_user = UserModel(
          id=generate(), 
          name=user.name, 
          email=user.email, 
          document=user.document,
          password=password,
          phone=user.phone
        )
      
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return db_user

