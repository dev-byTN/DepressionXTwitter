from database.database import *
from database.base import Base


if __name__ == "__main__":
    
    print("1- Create a dabase.")
    print("2- Save records.")
    print("3- Add a record.")
    print("4- Delete a record")
    print("5- Show database.")
    option = int(input("Choose an option: "))
    print("\n")
    
    match(option) :
        
        case 1:
            print("Database creation")
            Base.metadata.create_all(bind=engine)
            
        case 2:
            get_tweets()

        case 5:
            show_tweets