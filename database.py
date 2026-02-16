from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:Dansasuke12@rdsproj.cnwcewm0mb3c.ap-south-1.rds.amazonaws.com:5432/postgres?sslmode=require"

engine=create_engine(db_url,pool_pre_ping=True)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
