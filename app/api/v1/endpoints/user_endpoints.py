from fastapi.params import Depends
from fastapi import Request
from sqlalchemy.sql.functions import user
from app.main import app, get_db
from app.api.v1.providers import user_providers
from sqlalchemy.orm import Session
from app.schemas import schemas
from typing import List, Optional


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

@app.put("/api/v1/update_user/", tags=["User"])
def update_user(
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
    ):

    return user_providers.update_user(user, db)