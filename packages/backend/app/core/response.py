from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

# 定义一个可以代表任何类型的泛型变量 T
T = TypeVar("T")


class UnifiedResponseModel(BaseModel, Generic[T]):
    """
    统一API响应模型，支持泛型以实现精确的 `data` 类型提示。
    """

    code: int = Field(200, description="业务状态码, 200代表成功")
    msg: str = Field("success", description="响应消息")
    reqId: str = Field("", description="请求唯一ID")
    data: Optional[T] = Field(None, description="响应数据")
