from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

MYSQL_USER = os.getenv("MYSQLUSER", "root")
MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD", "zJICfmvmjBHIVMkHOSMvqUPIylZKamsL")
MYSQL_HOST = os.getenv("MYSQLHOST", "junction.proxy.rlwy.net")
MYSQL_PORT = os.getenv("MYSQLPORT", "14197")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "railway")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()