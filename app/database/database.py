from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base
from models.tweet import Tweet
from dotenv import load_dotenv
from models.tweet import readJsonFile, getRelevantData
import os

load_dotenv()
url = os.getenv("DATABASE_URL")

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_tweets():
    session = SessionLocal()
    
    try:
        fetch = readJsonFile()
        listOfTweets = getRelevantData(fetch)
        
        for i in listOfTweets:
            
            session.add(i)
            session.commit()
        print("Tweets saved in the database")
        
    finally:
        session.close()
        
        
def create_database():
    
    print("Database creation")
    Base.metadata.create_all(bind=engine)
    
    
def show_tweets():
    
    session = SessionLocal()
    try:
        tweet = session.query(Tweet).all()
        
        for i in tweet:
            print( f" {i.id}, {i.username}, {i.tweet}, {i.url}, {i.date}, {i.depressionType}, \
                    {i.createdAt}, {i.followers}, {i.following}, {i.photo}" )
            
    finally:
        session.close()