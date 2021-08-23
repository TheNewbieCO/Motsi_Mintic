from app.models.models import User
from datetime import datetime 
from fastapi import HTTPException,status 
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def generate_token(form_data,db):
    
    username = form_data.username
    password = form_data.password

    print(username)
    print(password)


    user_dict = db.query(User).filter(User.email == username).first()
    try:
        print('-'*10,type(user_dict),user_dict)

        if not user_dict:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        print('hola', 3)
        #salt = bcrypt.gensalt()
        #hashed_password_form = bcrypt.hashpw(form_data.password, salt)
        hashed_password_form = form_data.password
        #print('-'*10,hashed_password_form)
        print(hashed_password_form, 4)
        hashed_password_bd = user_dict.password
        #print('-'*10,hashed_password_bd)
        print(hashed_password_bd, 5)
        if hashed_password_form != hashed_password_bd:
        #if not checkpw(hashed_password_form.encode('utf8'), hashed_password_bd.encode('utf8')):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
            print("not match")

        return {"access_token": user_dict, "token_type": "bearer"}
    except Exception as e:
        return {"error": user_dict, "error_descr": "otra cosa"}
