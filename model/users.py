from sqlalchemy import Column, Integer, String, DateTime, func, select
from model.database import Base, engine, get_session
from loguru import logger


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    permission = Column(Integer, nullable=False, default=100)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)

    def get_user(self):
        try:
            with engine.connect() as conn:
                if self.id is not None:
                    query = select(Users).where(Users.id == self.id)
                elif self.name is not None:
                    query = select(Users).where(Users.name == self.name)
                res = conn.execute(query)
                logger.info("users query success")
                return res.scalar().all()
        except Exception as e:
            logger.error(f"Error: {e}")
            return None

    def add_user(self):
        try:
            with get_session() as session:
                session.add(self)
                session.commit()
                logger.info("users add success")
                return True

        except Exception as e:
            logger.error(f"Error: {e}")
            return False
        finally:
            session.close()


    def update_user(self):
        pass

    def delete_user(self):
        pass





