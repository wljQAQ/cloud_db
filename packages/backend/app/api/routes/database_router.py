from typing import List

from fastapi import APIRouter, Depends

from core.response import UnifiedResponseModel
from schemas.database_schema import DBConnect
from services.database_service import DatabaseService, database_service

router = APIRouter(prefix="/db", tags=["数据库"])


def get_db_service() -> DatabaseService:
    """依赖注入函数, 提供 DatabaseService 实例"""
    return database_service


@router.post(
    "/connect",
    response_model=UnifiedResponseModel,  # 声明成功响应的模型
    summary="测试数据库连接",
)
async def connect_test(
    connect_params: DBConnect,
    db_service: DatabaseService = Depends(get_db_service),
):
    """
    接收数据库连接参数，并测试连接的有效性。

    - **成功**: 返回标准的成功响应体。
    - **失败**: 全局异常处理器会自动捕获 BusinessException，并返回标准的错误响应体。
    """
    await db_service.connect_test(connect_params)

    # 如果上面的调用没有抛出异常，则代表连接成功
    return UnifiedResponseModel(data={"status": "ok", "message": "数据库连接成功！"})


@router.post(
    "/tables",
    response_model=UnifiedResponseModel[List[str]],  # 精确声明 data 的类型为字符串列表
    summary="获取所有表名",
)
async def get_all_tables(
    connect_params: DBConnect,
    db_service: DatabaseService = Depends(get_db_service),
):
    """
    根据提供的连接信息，获取数据库中的所有表名列表 (仅限 public schema)。
    """
    table_list = await db_service.get_tables(connect_params)
    return UnifiedResponseModel(data=table_list)
