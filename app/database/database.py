from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models.tweet import readJsonFile, getRelevantData
import os

load_dotenv()
url = os.getenv("DATABASE_URL")

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_tweets():
    db = SessionLocal()
    
    try:
        fetch = readJsonFile()
        listOfTweets = getRelevantData(fetch)
        
        for i in listOfTweets:
            
            db.add(i)
            db.commit()
        print("Tweets saved in the database")
        
    finally:
        db.close()