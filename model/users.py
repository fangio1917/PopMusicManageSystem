from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    permission = Column(Integer, nullable=False, default=100)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)



