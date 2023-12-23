from app.services.user import UserService
from sqlalchemy.orm import Session
from app.utils.auth import AuthUtil

class AuthService: 
    def authenticate_user(db: Session, username: str, password: str):
      user = UserService.get_user_by_email(db, username)
      if not user:
          return False
      if not AuthUtil.verify_password(password, user.password):
          return False
      return user