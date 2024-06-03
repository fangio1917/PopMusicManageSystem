from fastapi import FastAPI
from router.api_router import router_api
from middleware import auth_middleware


def create_app() -> FastAPI:
    app = FastAPI(root_path="/pmms")
    # 添加中间件
    app.middleware("http")(auth_middleware)

    # 添加路由
    app.include_router(router_api, prefix="/api")
    return app
