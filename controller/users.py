from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from model import Users
from fastapi import APIRouter

UserPydantic = sqlalchemy_to_pydantic(Users)

router_users = APIRouter()

@router_users.get("/users")
async def get_users():
	return {"message": "hello world"}
