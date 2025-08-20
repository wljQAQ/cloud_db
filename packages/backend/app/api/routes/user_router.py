from typing import List

from fastapi import APIRouter

from core.response import UnifiedResponseModel
from schemas.user_schema import UserSchema
from services import user_service

# 创建一个专门用于用户的路由器
# 我们可以更好地通过 tags 对API文档进行分组
router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    response_model=UnifiedResponseModel[List[UserSchema]],
    summary="获取所有用户列表",
)
async def read_users():
    """
    控制器层: 调用服务层获取所有用户。
    """
    users = user_service.get_all_users()
    return UnifiedResponseModel(data=users)


@router.get(
    "/{user_id}",
    response_model=UnifiedResponseModel[UserSchema],
    summary="根据ID获取单个用户",
)
async def read_user(user_id: int):
    """
    控制器层: 调用服务层获取单个用户。
    注意：这里不再需要try...except，因为服务层抛出的BusinessException
    会被全局异常处理器自动捕获。
    """
    user = user_service.get_user_by_id(user_id)
    return UnifiedResponseModel(data=user)
