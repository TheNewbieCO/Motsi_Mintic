from fastapi.params import Depends
from fastapi import Request
from fastapi.security import HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.sql.functions import user
from app.config.common import create_access_token
from app.models.models import User
from app.main import app, get_db
from app.api.v1.providers import user_providers
from sqlalchemy.orm import Session
from app.schemas import schemas
from typing import List, Optional
from fastapi import HTTPException
from app.config.common import oauth2_schema, decode_access_token

@app.get("/api/v1/get_all_users/", tags=["Users"], response_model=List[schemas.User])
def get_user(
    db: Session = Depends(get_db)
):
    db_user = db.query(User).all()
    return(db_user )

#------------ Get User (se optiene el usuario por medio del id)-----------------------------

@app.get("/api/v1/get_users/", tags=["Users"])
def get_user(
    token: str=Depends(oauth2_schema), 
    db: Session = Depends(get_db)
):
    dic_user= decode_access_token(token)

    return user_providers.get_user(dic_user.user_id, db)

@app.post("/api/v1/create_user/", tags=["Users"])
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    return user_providers.create_user(user, db)

@app.put("/api/v1/update_user/", tags=["Users"])
def update_user(user: schemas.UserUpdate,db: Session = Depends(get_db)):

    return user_providers.update_user(user, db)
    
@app.post("/api/v1/auth/")
async def  auth (data: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = User.autenticate(data.username, data.password, db)

    if user:
        return{
            "access_token": create_access_token(user)
            ,"token_type": "Bearer"
        }
    else :
        raise HTTPException(404,"Error al autentificar" )