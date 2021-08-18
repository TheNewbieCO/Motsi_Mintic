from pydantic.types import NoneStr
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime
from app.config.database import Base
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Amenity(BaseModel):

    id_activity: int
    id_amenity: int
    amenity_description: str
    amenity_media_file: str

    class Config:
        orm_mode = True

#------ schema Aves - Jose -- Se añadio "Aves" a "Activity"----------------------------

class Aves(BaseModel):
    id_activity: int
    aves_media_file: str

class TimeUnit(BaseModel):

    time_unit: str

    class Config:
        orm_mode = True
 
class Activity(BaseModel):
    id_activity: int   
    created_at: datetime = None
    activity_description: str
    activity_ammount: int
    updated_at: None
    activity_media_file: str
    amenities: List[Amenity] = []
    aves: List[Aves]=[]
    time_unit: TimeUnit = None

    class Config:
        orm_mode = True

class ActivityCreate(BaseModel):

    activity_description: str
    activity_media_file: str
    activity_ammount: int
    id_time_unit : int

class ActivityUpdate(BaseModel):

    id_activity: int
    activity_description: str
    activity_media_file: str
    activity_ammount: int
    id_time_unit : int

#--------- Schema User - Jose -----------------------------------
class User(BaseModel):

    id_user: int
    first_name:str
    second_name:str
    email:str
    password:str
    type_user: str
    user_media_file:str = None
    user_description: str=None
    activitys: List[Activity]=[]

    class Config:
        orm_mode = True

class UserCreate(BaseModel):

    first_name:str
    second_name:str
    email:str
    password:str
    type_user: str

class UserUpdate(BaseModel):

    first_name:str
    second_name:str
    email:str
    password:str
    user_media_file:str=None
    user_description: str=None