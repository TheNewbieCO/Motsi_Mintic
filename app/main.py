from fastapi import FastAPI, File, Form, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from app.models import models
#from .config.config import app_name
#from app.config.database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "",
    description = "MotsiApp",
    version = "0.1"
)

@app.get('/inicio')
async def ruta_de_prueba():
    return 'por finnnnn'