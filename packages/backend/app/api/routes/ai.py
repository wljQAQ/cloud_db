from typing import List

from fastapi import APIRouter, Depends
from openai import APIError

from core.ai import client
from core.config import settings
from core.exception_handler import BusinessException
from core.response import UnifiedResponseModel
from schemas.database_schema import DBConnect
from services.database_service import DatabaseService, database_service

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post(
    "/chat",
    summary="测试ai",
    response_model=UnifiedResponseModel[dict],
)
def chat():
    input_list = [
        {"role": "user", "content": "What is my horoscope? I am an Aquarius."}
    ]
    print(123)
    try:
        # 1. 创建流对象
        stream = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free",
            messages=input_list,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_horoscope",
                        "description": "Get today's horoscope for an astrological sign.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "sign": {
                                    "type": "string",
                                    "description": "An astrological sign like Taurus or Aquarius",
                                }
                            },
                            "required": ["sign"],
                        },
                    },
                }
            ],
            tool_choice="auto",
            stream=True,
        )

        # 2. 在 try 块内部处理整个流
        res = {}
        idx = 1
        tool_calls = {}

        for chunk in stream:
            # 建议使用 .model_dump() 以便序列化
            res[idx] = chunk.model_dump()
            idx += 1

            for tool_call in chunk.choices[0].delta.tool_calls or []:
                # 更健壮的 tool_calls 合并逻辑
                if tool_call.function and tool_call.function.arguments is not None:
                    index = tool_call.index
                    if index not in tool_calls:
                        tool_calls[index] = {
                            "id": tool_call.id,
                            "type": "function",
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": "",
                            },
                        }
                    tool_calls[index]["function"][
                        "arguments"
                    ] += tool_call.function.arguments

        # 3. 在 try 块的末尾返回成功响应
        return UnifiedResponseModel(
            data={
                "res": res,
                "tool_calls": tool_calls,
            },
            message="AI 响应成功",
        )

    except APIError as e:
        # 现在可以捕获流处理过程中的 API 错误了
        raise BusinessException(code=500, msg=f"AI 服务调用失败: {e.message}")
    except Exception as e:
        # 捕获其他所有未知异常
        raise BusinessException(code=500, msg=f"处理 AI 响应时发生未知错误: {str(e)}")
