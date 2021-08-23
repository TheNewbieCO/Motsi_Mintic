from fastapi.params import Depends
from app.main import app, get_db
from app.api.v1.providers import auth_providers
from sqlalchemy.orm import Session
#from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


@app.post("/token", tags=["OAuth2"])
def login(
    #form_data: OAuth2PasswordRequestForm = Depends(),
    form_data: schemas.UserLogin,
    db: Session = Depends(get_db)):
    return auth_providers.generate_token(form_data, db)



   