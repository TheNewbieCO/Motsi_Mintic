from datetime import datetime

from app.config.common import decode_access_token ,oauth2_schema
from app.main import get_db
from app.models.models import Activity2, Amenity
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import HTMLResponse
from fastapi import HTTPException


def get_all_activities( db, skip, limit):
    
    try: 
        db_activity = db.query(Activity2).offset(skip).limit(limit).all()

        return db_activity
    except Exception as e:
        print(e)
        return e
def get_all_user_activities(token =Depends(oauth2_schema),db: Session = Depends(get_db)):

    data= decode_access_token(token)

    if data:
        db_activities= db.query(Activity2).filter(Activity2.id_user== data["user_id"]).all()
        return db_activities
    else:
        raise HTTPException(401, "La sesión ha expirado")

        
def create_activity(activity,db):

    activity = Activity2(
        created_at = datetime.now(),
        activity_description = activity.activity_description,
        activity_ammount = activity.activity_ammount,
        activity_media_file = activity.activity_media_file,
        #id_time_unit = activity.id_time_unit        
        id_time_unit = 8 
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity



def update_activity(activity, db):

    update_object = {
        "activity_description" : activity.activity_description,  
        "activity_ammount": activity.activity_ammount,
        "activity_media_file" : activity.activity_media_file,
        "id_time_unit" : activity.id_time_unit
    }
#------------- cambie id_activity por activity.id_activity 
    db.query(Activity2).filter(Activity2.id_activity == activity.id_activity) \
        .update(update_object, synchronize_session='fetch')

    db.commit()
    db.refresh(update_object)

    return update_object
