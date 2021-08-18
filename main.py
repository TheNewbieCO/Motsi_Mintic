from fastapi import FastAPI

app = FastAPI()

@app.get('/inicio')
async def ruta_de_prueba():
    return 'por finnnnn'