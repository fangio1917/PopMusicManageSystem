from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import sql_dsn
from .users import Users

Base = declarative_base()

# 数据库连接
engine = create_engine(sql_dsn)


# # 数据库回话，属于事务处理
# def get_session():
#     db_session = sessionmaker(bind=engine)
#     session = db_session()
#     return session

__all__ = ['Base', 'engine', 'Users']

