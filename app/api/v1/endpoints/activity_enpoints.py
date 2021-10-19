from fastapi.params import Depends
from fastapi import Request
from app.main import app, get_db
from app.api.v1.providers import activity_providers
from sqlalchemy.orm import Session
from app.models.models import Activity, Activity2
from app.schemas import schemas
from typing import List, Optional

@app.get("/api/v1/get_activities/", tags=["Activities"], response_model=List[schemas.Activity2])
def get_activities(id: int = 0, db: Session = Depends(get_db), skip:int = 0, limit:int = 10):
    try:
        return activity_providers.get_all_activities(db, skip, limit)
    except Exception as e:
        return (e)

@app.get("/api/v1/get_user_activities/", tags=["Users-Activities"])
def get_user( activity: Activity2=Depends(activity_providers.get_all_user_activities)):

    return activity
        
@app.post("/api/v1/create_activty/", tags=["Activities"])

def create_activity(
    activity: schemas.ActivityCreate,
    db: Session = Depends(get_db)):
    try:
        return activity_providers.create_activity(activity, db)
    except Exception as e:
        return (e)

@app.put("/api/v1/update_activity/", tags=["Activities"])
def update_activity(
    activity: schemas.ActivityUpdate,
    db: Session = Depends(get_db)
    ):
    try:

        return activity_providers.update_activity(activity, db)
    except Exception as e:
        return (e)