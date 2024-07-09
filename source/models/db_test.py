from sqlalchemy import Column, Integer, String, Float , DECIMAL
from sqlalchemy.ext.declarative import declarative_base

#Database Table
class db_tests(declarative_base()):

    __tablename__ = 'db_test'

    testData = Column(String(10),primary_key=True)