# lib/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the declarative Base and engine
Base = declarative_base()
engine = create_engine('sqlite:///inventory.db', echo=True)  # echo=True for helpful logging

# Configure the session factory
Session = sessionmaker(bind=engine)
session = Session()
