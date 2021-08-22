from app.models.models import User
from datetime import datetime 
from fastapi import HTTPException,status 
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def generate_token(form_data,db):
    user_dict = db.query(User).filter(User.email == form_data.username)
    print('-'*10,user_dict)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    salt = bcrypt.gensalt()
    hashed_password_form = bcrypt.hashpw(form_data.password, salt)
    print('-'*10,hashed_password_form)
    hashed_password_bd = user_dict['password']
    print('-'*10,hashed_password_bd)
    if bcrypt.checkpw(hashed_password_form, hashed_password_bd):
#    if not hashed_password_form == hashed_password_bd:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        print("match")
    return {"access_token": form_data.username, "token_type": "bearer"}
