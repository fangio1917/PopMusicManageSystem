from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from model import Base


# 定义 Songs 表
class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    singer = Column(String(1024), nullable=False)
    album = Column(String(255), nullable=False)
    date = Column(DateTime)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)