from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Products(Base):

    __tablename__="DMARKET"

    id =Column(Integer,primary_key=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)
