from sqlalchemy.sql.functions import user
from app.models.models import Activity, Amenity, User
from datetime import datetime

#------------ Obtiene el usuario por la id y retorna la información del user ------------------

def get_user(id_user, db):

    db_user = db.query(User).filter(User.id_user == id_user).first()
    
    return db_user

def create_user(user,db):

    user = User(
        first_name = User.first_name,
        second_name = User.second_name,
        email = User.email,
        password = User.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def update_user(user, db):

    update_object = {
        "user_description" : user.user_description,  
        "first_name": user.first_name,
        "second_name": user.second_name,
        "user_media_file" : user.user_media_file,
        "email": user.email,
        "password": user.password    
        }

    db.query(User).filter(User.id_user == user.id_user) \
        .update(update_object, synchronize_session='fetch')

    db.commit()
    db.refresh(update_object)

    return update_object