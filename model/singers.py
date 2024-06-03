from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from model import Base

# 定义 Singers 表
class Singer(Base):
    __tablename__ = 'singers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    birth_date = Column(DateTime)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)