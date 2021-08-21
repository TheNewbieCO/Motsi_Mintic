from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from app.config.database import Base
import passlib.hash as _hash
import bcrypt


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
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, index=True)
    first_name= Column(String)
    second_name= Column(String)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    created_at = Column(String)
    update_at = Column(DateTime)
    rnt = Column(String)
    id_role = Column(Integer, ForeignKey("role.id_role"))

    def verify_pass(self, password_form: str):
        return __hash.bcrypt.verify(password_form, self.hashed_password)

class TimeUnit(Base):
    __tablename__ = "time_unit"
    id_time_unit = Column(Integer, primary_key=True, index=True)
    time_unit = Column(String)

class Amenity(Base):
    __tablename__ = "amenity"

    id_amenity= Column(Integer, primary_key=True, index=True)
    amenity_description = Column(String)
    amenity_media_file = Column(String)

    id_activity = Column(Integer, ForeignKey("activity.id_activity"))

#-------Clase de Aves - Jose ---------
class Aves(Base):
    __tablename__="aves"

    id_aves= Column(Integer, primary_key=True, index=True)
    amenity_media_file = Column(String)
    id_activity = Column(Integer, ForeignKey("activity.id_activity"))



class Activity(Base):
    __tablename__ = "activity"

    id_activity = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("user.id_user"))
    activity_description = Column(String)
    activity_media_file = Column(String)
    activity_ammount = Column(Integer)
    id_time_unit = Column(Integer, ForeignKey("time_unit.id_time_unit"))

    amenities = relationship("Amenity")
    aves= relationship("Aves")
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



