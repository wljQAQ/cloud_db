import time
import uuid
from fastapi import Request, Response


async def add_process_time_header(request: Request, call_next) -> Response:
    """
    中间件，用于处理以下任务:
    1. 为每个请求生成一个唯一的请求ID (req_id)。
    2. 将 req_id 附加到 request.state，以便在应用内部访问。
    3. 在响应头中添加 X-Request-ID。
    4. 在响应头中添加 X-Process-Time，记录请求处理时间。
    """
    start_time = time.time()
    req_id = str(uuid.uuid4())

    # 将req_id附加到请求状态
    request.state.req_id = req_id

    # 调用下一个中间件或路由处理器
    response: Response = await call_next(request)

    # 计算处理时间并添加到响应头
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"

    # 将req_id添加到响应头
    response.headers["X-Request-ID"] = req_id

    return response
