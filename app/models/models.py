from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
import hashlib


from app.config.database import Base




class Role(Base):
    __tablename__ =  "role"

    id_role = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)

#TENER PRESENTE: que cuando se agregan nuevos campos al modelo, se crea una tabla nueva
#TENER PRESENTE: versionamiento en BD ALLembic (para hacer migraciones)
#TENER PRESENTE: podria buscarse una api que guarde imagenes y devuelva links 
#TENER PRESENTE: en fastapi hay algo que "monta una unidad" donde se guardan los archivos, para generarle una ruta (dentro del mismo servidor)


#--------------- Se agregó el Nombre y Apellido del usuario---------------
#--------------- username y correo son los mismos -----------------------

class User(Base):
    __tablename__ = "user3" 

    id_user = Column(Integer, primary_key=True, index=True)
    first_name= Column(String)
    second_name= Column(String)
#   username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    type_user = Column(String)


    @classmethod
    def autenticate(cls, username, password, db):
        user = db.query(User).filter(User.email == username).first()

        if user and user.password == cls.create_password(password):
            print("La contraseña si es correcta")
            return user
        print('-'*50,user)
        print('-'*50,db.query(User))

        
    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode("utf-8"))
        return h.hexdigest()

class TimeUnit(Base):
    __tablename__ = "time_unit"
    id_time_unit = Column(Integer, primary_key=True, index=True)
    time_unit = Column(String)

class Amenity(Base):
    __tablename__ = "amenity"
    id_amenity= Column(Integer, primary_key=True, index=True)
    amenity_description = Column(String)
    amenity_media_file = Column(String)
    id_user = Column(Integer, ForeignKey("User.id_user"))

#-------Clase de Aves - Jose ---------
class Aves(Base):
    __tablename__="aves"

    id_aves= Column(Integer, primary_key=True, index=True)
    amenity_media_file = Column(String)
    """ 
    id_activity = Column(Integer, ForeignKey("activity.id_activity")) """



class Activity2(Base):
    __tablename__ = "activity2"

    id_activity = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer)
    activity_description = Column(String)
    activity_media_file = Column(String)
    activity_ammount = Column(Integer)
    id_time_unit = Column(Integer, ForeignKey("time_unit.id_time_unit"))

    """ amenities = relationship("Amenity")
    aves= relationship("Aves") """
    time_unit = relationship("TimeUnit")

class Service(Base):
    __tablename__ = "service"

    id_service = Column(Integer, primary_key=True, index=True)
    service_description = Column(String)
    service_offered_date = Column(DateTime)
    service_media_file = Column(String)

    id_time_unit = Column(Integer, ForeignKey("time_unit.id_time_unit"))

class Booking(Base):
    __tablename__ = "booking"

    id_booking = Column(Integer, primary_key=True, index=True)
    booking_date = Column(DateTime)


class Review(Base):
    __tablename__ = "review"

    id_review = Column(Integer, primary_key=True, index=True)
    review = Column(String)
    
    id_booking = Column(Integer, ForeignKey("booking.id_booking"))