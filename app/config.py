from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:asdqwe123@127.0.0.1:3306/inbody"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("SESSION LOCAL :: ", SessionLocal)

Base = declarative_base()