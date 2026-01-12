from database.database import *
from database.base import Base

if __name__ == "__main__":
    
    while(True):
        
        print("1- Create a dabase.")
        print("2- Save records.")
        print("3- Add a record.")
        print("4- Delete a record")
        print("5- Show database.")
        print("6- Quit.")
        
        option = int(input("Choose an option: "))
        print("\n")
        
        match(option):
            
            case 1:
                print("Database creation")
                Base.metadata.create_all(bind=engine)
                break
                
            case 2:
                get_tweets()
                break

            case 3:
                nb_user = int(input("How many users fo you want to add in the database: "))
                add_record(nb_user)
                break
            
            case 4:
                id = int(input("Enter the id of the user you want to delete: "))
                delete_record(id)
                break
                
            case 5:
                show_tweets()
                break
                
            case 6:
                session.close()
                break
            