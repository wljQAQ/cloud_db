from typing import List

from fastapi import APIRouter, Depends

from core.response import UnifiedResponseModel
from schemas.database_schema import DBConnect
from services.database_service import DatabaseService, database_service
from core.config import settings
from core.ai import client, tools

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post(
    "/chat",
    summary="测试ai",
)
def chat():

    input_list = [
        {"role": "user", "content": "What is my horoscope? I am an Aquarius."}
    ]

    print(settings.open_router_base_url, settings.open_router_deepseek_api_key)

    stream = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=input_list,
        tools=[
            {
                "type": "function",
                # 这里有个坑 openrouter需要在套一层function 最新的openai规范不需要
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

    res = {}

    idx = 1

    tool_calls = {}

    for chunk in stream:
        res[idx] = chunk
        idx += 1

        for tool_call in chunk.choices[0].delta.tool_calls or []:
            index = tool_call.index
            if index not in tool_calls:
                tool_calls[index] = tool_call

            tool_calls[index].function.arguments += tool_call.function.arguments

        print(chunk)

    return {
        "res": res,
        "tool_calls": tool_calls,
    }
