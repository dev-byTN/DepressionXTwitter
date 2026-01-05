from database.database import engine, get_tweets
from database.base import Base


if __name__ == "__main__":
    
    print("Database creation")
    Base.metadata.create_all(bind=engine)
    get_tweets()
    