from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, select, and_, or_
from model.database import Base, get_session
from loguru import logger


# 定义 Songs 表
class Songs(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    singer = Column(String(1024), nullable=False)
    album = Column(String(255), nullable=False)
    date = Column(DateTime)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
    
    def add_song(self):
        # 添加歌曲到数据库
        try:
            with get_session() as session:
                session.add(self)
                session.commit()
                logger.info(f"Song {self.name} added successfully.")
                return True
            
        except Exception as e:
            logger.error(f"Failed to add song: {e}")
            return False
        finally:
            session.close()
    
    def get_songs(self):
        # query songs
        try:
            with get_session() as session:
                
                query = select(Songs).where(Songs.deleted_at.is_(None))
                query_condition = []
                if self.id is not None:
                    query = query.where(Songs.id == self.id)
                    res = session.execute(query)
                    return res.scalars().all()
                
                if self.name is not None:
                    query_condition.append(Songs.name == self.name)
                
                if self.singer is not None:
                    query_condition.append(Songs.singer == self.singer)
                    
                if self.album is not None:
                    query_condition.append(Songs.album == self.album)
                    
                query = query.where(or_(*query_condition))
                res = session.execute(query)
                return res.scalars().all()
            
        except Exception as e:
            logger.error(f"Failed to get songs: {e}")
            return False
        
        finally:
            session.close()
        
    def update_songs(self):
        try:
            with get_session() as session:
                session.query(Songs).filter(Songs.id == self.id and Songs.deleted_at.is_(None)).update({
                    'name': self.name,
                    'singer': self.singer,
                    'album': self.album,
                    'date': self.date,
                    'url': self.url,
                    'updated_at': func.now()
                })
                session.commit()
                logger.info("Songs update success")
                return True

        except Exception as e:
            logger.error(f"Error: {e}")
            return False
        finally:
            session.close()
            
    def delete_songs(self):
        try:
            with get_session() as session:
                session.query(Songs).filter(Songs.id == self.id and Songs.deleted_at.is_(None)).update({
                    'deleted_at': func.now()
                    
                })
                session.commit()
                logger.info("Songs delete success")
                return True
            
        except Exception as e:
            logger.error(f"Error: {e}")
            return False
        
        finally:
            session.close()
        
    def exist_songs(self):
        # 检查歌曲是否存在
        try:
            with get_session() as session:
                
                query = select(Songs).where(Songs.id == self.id)
                res = session.execute(query)
                return res.scalars().first()
            
        except Exception as e:
            logger.error(f"Failed to check songs: {e}")
            return False
        finally:
            session.close()