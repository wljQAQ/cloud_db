from fastapi import APIRouter, FastAPI

# 导入新的用户路由
from . import user_router


# 初始化路由
def init_all_routes(app: FastAPI) -> None:
    """初始化所有路由"""
    base_router = APIRouter(prefix="/api/v1")

    # 注册用户路由
    base_router.include_router(user_router.router)

    # 如果未来有产品路由(product_router)，也在这里注册
    # base_router.include_router(product_router.router)

    app.include_router(base_router)
