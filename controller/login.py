from fastapi import APIRouter, status
from model.users import Users
from .users import UserPydantic
from datetime import datetime, timedelta
import jwt
from config import SECRET_KEY, ALGORITHM

login = APIRouter()


def create_token(username: str) -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)
    to_encode = {"exp": expiration, "sub": username}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@login.post("/login")
async def login(user: UserPydantic):
    try:
        login_user = Users(
            name=user.name,
        )
        login_user.get_user()
        if login_user is None:
            raise Exception("User not found")
        if login_user.password != user.password:
            raise Exception("Password is incorrect")

        token = create_token(login_user.name)

        return {"message": "Login successful", "Authorization": token}, status.HTTP_200_OK

    except Exception as e:
        return {"message": str(e)}, status.HTTP_400_BAD_REQUEST






