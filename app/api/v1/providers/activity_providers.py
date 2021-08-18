from app.models.models import Activity, Amenity
from datetime import datetime

def get_all_activities(id_activity, db, skip, limit):

    if id_activity != 0:
        db_activity = [db.query(Activity).filter(Activity.id_activity == id_activity).first()]
    else:
        db_activity = db.query(Activity).offset(skip).limit(limit).all()

    return db_activity

def create_activity(activity,db):

    activity = Activity(
        created_at = datetime.now(),
        activity_description = activity.activity_description,
        activity_ammount = activity.activity_ammount,
        activity_media_file = activity.activity_media_file,
        id_time_unit = activity.id_time_unit
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
    db.query(Activity).filter(Activity.id_activity == activity.id_activity) \
        .update(update_object, synchronize_session='fetch')

    db.commit()
    db.refresh(update_object)

    return update_object