from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, status, Response
from model.songs import Song


class SongPydantic(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    singer: Optional[str] = None
    album: Optional[str] = None
    date: Optional[datetime] = None
    url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    
    
router_songs = APIRouter()


@router_songs.post("/add", status_code=status.HTTP_201_CREATED)
async def add_song(a_song: SongPydantic, response: Response):
    try:
        
        added_song = Song(**a_song.dict())
        
        added_song.add_song()
        
        return {"message": "Song added successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}
        
        
@router_songs.get("/query", status_code=status.HTTP_200_OK)
async def get_songs(response: Response,
                    queried_id: Optional[int] = None,
                    queried_name: Optional[str] = None,
                    queried_singer: Optional[str] = None,
                    queried_album: Optional[str] = None,
                    queried_date: Optional[datetime] = None,
                    ):
    try:
        
        queried_songs = Song(
            id=queried_id,
            name=queried_name,
            singer=queried_singer,
            album=queried_album
        )
        
        queried_songs = queried_songs.get_songs()
        if len(queried_songs) == 0:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No songs found"}
        
        return {"message": "Songs found", "data": queried_songs}
    
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}
    
    
@router_songs.put("/update", status_code=status.HTTP_200_OK)
async def update_song(u_song: SongPydantic, response: Response):
    try:
        updated_song = Song(
            id=u_song.id,
        )
        existed = updated_song.exist_songs()
        if existed is False or existed is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Song not found"}
        
        if u_song.name is not None:
            existed.name = u_song.name
        if u_song.singer is not None:
            existed.singer = u_song.singer
        if u_song.album is not None:
            existed.album = u_song.album
            
        if existed.update_songs():
            return {"message": "Song updated successfully"}
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Song not updated"}
        
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}
        
        
@router_songs.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_song(deleted_id: int, response: Response):
    
    try:
        
        deleted_song = Song(
            id=deleted_id
        )
        
        deleted = deleted_song.delete_songs()
        
        if deleted is True:
            
            return {"message": "Song deleted successfully"}
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Song not deleted"}
    
    except Exception as e:
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}
        