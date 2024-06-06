from fastapi import APIRouter
from controller.users import router_users
from controller.songs import router_songs
from controller.file import router_file


router_api = APIRouter()

router_api.include_router(router_users, prefix="/users")
router_api.include_router(router_songs, prefix="/songs")
router_api.include_router(router_file, prefix="/file")
