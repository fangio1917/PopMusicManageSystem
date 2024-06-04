from fastapi import FastAPI
from router.api_router import router_api
from controller.login import router_login
from router.middleware import AuthMiddleware


app = FastAPI()

app.include_router(router_login)

api_app = FastAPI()
api_app.include_router(router_api)
api_app.middleware("http")(AuthMiddleware)
# 将子应用程序挂载到主应用程序
app.mount("/api", api_app)

