import uvicorn
from fastapi import FastAPI

from api import init_api
from core.middleware import add_process_time_header
from core.exception_handler import init_exception_handlers

# 实例化FastAPI应用
app = FastAPI()

# 注册中间件
app.middleware("http")(add_process_time_header)

# 初始化全局异常处理器
init_exception_handlers(app)

# 初始化API路由
init_api(app)
# 启动服务
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True, log_level="info")
