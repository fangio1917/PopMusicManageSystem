from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from model import Users
from fastapi import APIRouter, status

router_users = APIRouter()


class UserPydantic(BaseModel):
    id: int
    name: Optional[str] = None
    password: Optional[str] = None
    permission: Optional[int] = 100
    url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


@router_users.post("/add")
async def add_user(added_user: UserPydantic):
    try:
        user_created = Users(
			name=added_user.name,
			password=added_user.password,
			permission=added_user.permission,
        )




@router_users.get("/query")
async def get_users(queried_id: int):
    queried_user = Users(
        id=queried_id,
    )
    try:
        responses = queried_user.get_user()
    except Exception as e:
        return {"success": False, "message": str(e)}, status.HTTP_400_BAD_REQUEST

    return {"success": True, "data": responses}, status.HTTP_200_OK
