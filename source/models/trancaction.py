from sqlalchemy import Column, Integer, String, Float , DECIMAL
from sqlalchemy.ext.declarative import declarative_base

#Database Table
class transactions (declarative_base()):

    __tablename__ = 'transactions'

    id          = Column(Integer,primary_key=True)
    amount      = Column(Float)
    category    = Column(String(100))
    description = Column(String(100))
    is_income   = Column(Integer)
    date        = Column(String(20))