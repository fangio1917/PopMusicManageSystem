from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from model import Base


# 定义 Albums 表
class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    release_date = Column(DateTime)
    singer = Column(String(1024), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
