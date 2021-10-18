from fastapi.params import Depends
from fastapi import Request
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.sql.functions import user
from app.models.models import User
from app.main import app, get_db
from app.api.v1.providers import user_providers
from sqlalchemy.orm import Session
from app.schemas import schemas
from typing import List, Optional
from fastapi import HTTPException

@app.get("/api/v1/get_all_users/", tags=["Users"], response_model=List[schemas.User])
def get_user(
    db: Session = Depends(get_db)
):
    db_user = db.query(User).all()
    return(db_user )

#------------ Get User (se optiene el usuario por medio del id)-----------------------------

@app.get("/api/v1/get_users/", tags=["Users"], response_model=List[schemas.User])
def get_user(
    id: int, 
    db: Session = Depends(get_db)
):

    return user_providers.get_user(id, db)

@app.post("/api/v1/create_user/", tags=["Users"])
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    return user_providers.create_user(user, db)

@app.put("/api/v1/update_user/", tags=["Users"])
def update_user(
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
    ):

    return user_providers.update_user(user, db)

@app.post("/api/v1/login/", response_model=List[schemas.UserLogin])
def login(credentials: HTTPBasicCredentials, response:Response):
    user= User.select().where(User.email==credentials.username).first()

    if user is None:
        raise HTTPException(404, "User not found")
    if user.password !=User.create_password(credentials.password):
        raise HTTPException(404, "Password error")

    return user
    