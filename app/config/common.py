from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, oauth2
import jwt
from datetime import datetime, timedelta
from ..models.models import User
from sqlalchemy.orm import Session
from ..main import get_db

SECRET_KEY = 'Motsi-Mintic-Backend-Airbnb2008'


oauth2_schema= OAuth2PasswordBearer(tokenUrl="/api/v1/auth/")

def create_access_token(user,days=30):

    data={
        "user_id":user.id_user,
        "username":user.email,
        "exp":datetime.utcnow() + timedelta(seconds=days)
    }
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")





def decode_access_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms="HS256")





def get_current_user ( token: str = Depends(oauth2_schema), db: Session = Depends(get_db) ) ->User :

    data= decode_access_token(token)

    db_user = db.query(User).filter(User.id_user == data["user_id"]).first()
    
    return db_user
