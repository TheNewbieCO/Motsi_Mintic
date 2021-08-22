from fastapi.params import Depends
from fastapi import Depends,FastAPI,HTTPException,status
from app.main import app, get_db
from app.api.v1.providers import activity_providers
from sqlalchemy.orm import Session
from app.schemas import schemas
from typing import List, Optional
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_dict = db.query(users).filter_by(name = form_data.username)
    if not user_dict:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    salt = bcrypt.gensalt()
    hashed_password_form = bcrypt.hashpw(form_data.password, salt)
    hashed_password_bd = user_dict['password']
    if bcrypt.checkpw(hashed_password_form, hashed_password_bd):
#    if not hashed_password_form == hashed_password_bd:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        print("match")

    return {"access_token": user.username, "token_type": "bearer"}


