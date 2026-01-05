from app.database.database import base
from app.database.base import Base


if __name__ == "__main__":
    print("Database creation")
    Base.metadata.create_all(bind=engine)