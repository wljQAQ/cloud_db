from fastapi import APIRouter, FastAPI

from .table_curd import router as table_curd_router


# 初始化路由
def init_all_routes(app: FastAPI) -> None:
    "初始化所有路由"
    base_router = APIRouter(prefix="/v1/api")
    base_router.include_router(table_curd_router)

    app.include_router(base_router)
