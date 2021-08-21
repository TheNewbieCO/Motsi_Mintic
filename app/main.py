from fastapi import FastAPI, File, Form, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import models
from .config.config import app_name
from app.config.database import SessionLocal, engine
from fastapi_login import LoginManager

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

SECRET="9117515f7ac53aa8e13eab8410ffb145a5b59cd3cbfebfae"

manager= LoginManager(SECRET, '/login')

@manager.user_loader
def query_user(id_user:str):
    base = db.query(User).filter(User.id_user == id_user).first()

    return ()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Motsi Backend" : "It's alive!!!"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.api import endpoints_call
# import sys

@app.get('/inicio')
async def ruta_de_prueba():
    return 'por finnnnn'