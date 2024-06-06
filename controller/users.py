from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from model import Users
from fastapi import APIRouter, status, Response

router_users = APIRouter()


class UserPydantic(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str] = None
    permission: Optional[int] = 100
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


@router_users.get("/")
def read_root():
    return {"Hello": "World"}


@router_users.post("/add", status_code=status.HTTP_201_CREATED)
async def add_user(added_user: UserPydantic, response: Response):
    try:
        user_created = Users(
            name=added_user.name,
            password=added_user.password,
            permission=added_user.permission,
            created_at=datetime.now(),
        )
        user_created.add_user()

    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    return {"success": True, "data": "User created"}


@router_users.put("/update", status_code=status.HTTP_200_OK)
async def update_user(updated_user: UserPydantic, response: Response):
    try:
        if updated_user.id is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"success": False, "message": "User id is required"}
        user_updated = Users(id=updated_user.id)
        
        existed = user_updated.exist_user()
        
        if existed is None or existed is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"success": False, "message": "User not found"}
        
        if updated_user.name is not None:
            existed.name = updated_user.name
            
        if updated_user.password is not None:
            existed.password = updated_user.password
        
        if updated_user.permission is not None:
            existed.permission = updated_user.permission
            
        existed.update_user()
        
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}
    
    return {"success": True, "data": "User updated"}


@router_users.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_user(deleted_id: int, response: Response):
    
    try:
        if deleted_id is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"success": False, "message": "User id is required"}
        user_deleted = Users(id=deleted_id)
        user_deleted.delete_user()
        return {"success": True, "data": "User deleted"}
        
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}


@router_users.get("/query", status_code=status.HTTP_200_OK)
async def get_users(response: Response):
    queried_user = Users()
    try:
        resp = queried_user.get_user()
        if len(resp) == 0:
            raise Exception("back empty")

        class ret(BaseModel):
            id: Optional[int] = None
            name: Optional[str] = None
            permission: Optional[str] = None
       
        datas = []
        for res in resp:
            data = ret()

            data.id = res.id

            data.name = res.name
            if res.permission == 1:
                data.permission = "root"

            elif res.permission == 10:
                data.permission = "admin"

            elif res.permission == 100:
                data.permission = "user"
            else:
                data.permission = "other"

            datas.append(data)

    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"success": False, "message": str(e)}

    return {"success": True, "data": datas}
