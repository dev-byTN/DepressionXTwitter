from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.base import Base
from models.tweet import Tweet
from dotenv import load_dotenv
from models.tweet import readJsonFile, getRelevantData
import os

load_dotenv()
url = os.getenv("DATABASE_URL")

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def get_tweets():
    
    try:
        fetch = readJsonFile()
        listOfTweets = getRelevantData(fetch)
        session.add_all(listOfTweets)
        session.commit()
        print("Tweets saved in the database.\n")
        
    except SQLAlchemyError as e:
        session.rollback()
        print("Error creating the database.\n", e)    
        
        
def create_database():
    
    print("Database creation")
    Base.metadata.create_all(bind=engine)
    
    
def show_tweets():
    
    try:
        tweet = session.query(Tweet).all()
        
        for i in tweet:
            print( f" {i.id}, {i.username}, {i.tweet}, {i.url}, {i.date}, {i.depressionType}, \
                    {i.createdAt}, {i.followers}, {i.following}, {i.photo}" )
            
        print("\n")
        
    except SQLAlchemyError as e:
        session.rollback()
        print("Error accessing the databse.\n", e)
        
        
def add_record(user):
    
    try:
        session.add(user)
        session.commit()
        print("Record(s) added succesfully.\n")
    
    except SQLAlchemyError as e:
        session.rollback()
        print("Error adding user(s) into the database\n", e)
        
        
def get_users_id():
    
    list = []
    try:
        user = session.query(Tweet).all()
        
        for i in user:
            username = user["username"]
            id = user["id"]
            
            record = [id, username]
            list.append(record)
            
        session.commit()
        
    except SQLAlchemyError as e:
        session.rollback()
        print("Error fetching users.\n", e)
        
    return list


def delete_record(id):
    
    try:
        session.query(Tweet).filter(Tweet.id == id).delete()
        session.commit()
        print("Record deleted succesfully.\n")
        
    except SQLAlchemyError as e:
        session.rollback()
        print("No user with that id in the database.\n", e)