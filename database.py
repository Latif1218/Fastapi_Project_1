from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:4321@localhost/Pizza_Delivery_project'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo= True)

Base = declarative_base()

session = sessionmaker()