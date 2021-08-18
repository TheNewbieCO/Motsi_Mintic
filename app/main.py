from fastapi import FastAPI, File, Form, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import models
from .config.config import app_name
from app.config.database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

#from app.api import endpoints_call
# import sys

@app.get('/inicio')
async def ruta_de_prueba():
    return 'por finnnnn'