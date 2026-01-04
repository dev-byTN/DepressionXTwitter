from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from app import tweet

load_dotenv()
url = os.getenv("DATABASE_URL")

engine = create_engine(url)
session = sessionmaker(autocomit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    
    try:
        yield db
    finally:
        db.close()