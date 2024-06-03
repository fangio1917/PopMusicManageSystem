# middlewares.py
from fastapi import Request, HTTPException
import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM


# 创建 JWT 令牌的函数
def create_token(username: str, password: str) -> str:
    expiration = datetime.utcnow() + timedelta(hours=1)
    to_encode = {"exp": expiration, "sub": username}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def auth_middleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    response = await call_next(request)
    return response
