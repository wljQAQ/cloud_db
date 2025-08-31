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


    response = client.chat.completions.create(
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
    )

    print(response)

    return response
