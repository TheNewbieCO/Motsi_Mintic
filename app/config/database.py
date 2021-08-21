  
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.config import config

from datetime import datetime

user = 'uqlblnzxwauflm'
password = "c388f153ad80dc089ef09946c644277e38fb7c98400ef65fe07888b2608fc752"
database = 'df2tf43nht9t45'
host = 'ec2-34-194-14-176.compute-1.amazonaws.com'
port = 5432


# user = config['databases']['postgresql']['user'].get()
# password = config['databases']['postgresql']['password'].get()
# database = config['databases']['postgresql']['database'].get()
# host = config['databases']['postgresql']['host'].get()
# port = config['databases']['postgresql']['port'].get()

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import Column
from sqlalchemy import DateTime

class CustomBase(object):

    __abstract__ = True

    created_at = Column(DateTime(), default = datetime.now(), index=True)
    updated_at = Column(DateTime(), onupdate = datetime.now(), index=True)

Base = declarative_base(cls=CustomBase)