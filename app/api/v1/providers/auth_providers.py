from app.models.models import User
from datetime import datetime 
from fastapi import HTTPException,status 
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def generate_token(form_data,db):
    try:
        user_dict = db.query(User).filter(User.email == form_data.username).first()
        #print('-'*10,user_dict.values())

        if not user_dict:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        salt = bcrypt.gensalt()
        #hashed_password_form = bcrypt.hashpw(form_data.password, salt)
        hashed_password_form = form_data.password
        print('-'*10,hashed_password_form)
        hashed_password_bd = user_dict['password']
        print('-'*10,hashed_password_bd)
        
        if hashed_password_form != hashed_password_bd:
        #if not checkpw(hashed_password_form.encode('utf8'), hashed_password_bd.encode('utf8')):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
            print("not match")

        return {"access_token": User.email, "token_type": "bearer"}
    except Exception as e:
        return {"error": user_dict, "error_descr": "otra cosa"}
