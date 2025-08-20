from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .response import UnifiedResponseModel


class BusinessException(Exception):
    """
    自定义业务异常类，用于在业务逻辑中主动抛出错误。
    """

    def __init__(self, code: int, msg: str, data: any = None):
        self.code = code
        self.msg = msg
        self.data = data


def init_exception_handlers(app: FastAPI) -> None:
    """注册全局异常处理器"""

    @app.exception_handler(BusinessException)
    async def business_exception_handler(request: Request, exc: BusinessException):
        """处理自定义的业务异常"""
        req_id = getattr(request.state, "req_id", "")
        # 对于业务异常，我们总是返回HTTP 200 OK，但在响应体中指明错误
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=UnifiedResponseModel(
                code=exc.code, msg=exc.msg, data=exc.data, reqId=req_id
            ).model_dump(),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        """处理请求数据验证错误 (Pydantic模型验证失败)"""
        req_id = getattr(request.state, "req_id", "")
        # 从异常中提取更易读的错误信息
        error_msgs = [f"{err['loc'][-1]}: {err['msg']}" for err in exc.errors()]
        detail = "; ".join(error_msgs)
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=UnifiedResponseModel(
                code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                msg=f"请求参数校验失败: {detail}",
                reqId=req_id,
            ).model_dump(),
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """处理FastAPI定义的HTTP异常 (如404 Not Found)"""
        req_id = getattr(request.state, "req_id", "")
        return JSONResponse(
            status_code=exc.status_code,
            content=UnifiedResponseModel(
                code=exc.status_code, msg=exc.detail, reqId=req_id
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """处理所有其他未被捕获的全局异常"""
        req_id = getattr(request.state, "req_id", "")
        # 在生产环境中，为了安全不应暴露详细的错误信息
        # 此处可以添加日志记录: logging.error(str(exc))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=UnifiedResponseModel(
                code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                msg="服务器内部错误",
                reqId=req_id,
            ).model_dump(),
        )
