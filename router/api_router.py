from fastapi import APIRouter
from controller.users import router_users


router_api = APIRouter()

router_api.include_router(router_users, prefix="/users")
