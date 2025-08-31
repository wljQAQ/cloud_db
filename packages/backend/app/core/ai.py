from openai import OpenAI

from core.config import settings

client = OpenAI(
    base_url=settings.open_router_base_url,
    api_key=settings.open_router_deepseek_api_key,
)


tools = [
    # {
    #     "type": "function",
    #     "name": "get_weather",
    #     "description": "查询给定地点的当前天气.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "location": {
    #                 "type": "string",
    #                 "description": "City and country e.g. Bogotá, Colombia",
    #             },
    #             "units": {
    #                 "type": "string",
    #                 "enum": ["celsius", "fahrenheit"],
    #                 "description": "Units the temperature will be returned in.",
    #             },
    #         },
    #         "required": ["location"],
    #     },
    # },
    # {
    #     "type": "function",
    #     "name": "get_horoscope",
    #     "description": "Get today's horoscope for an astrological sign.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "sign": {
    #                 "type": "string",
    #                 "description": "An astrological sign like Taurus or Aquarius",
    #             },
    #         },
    #         "required": ["sign"],
    #     },
    # },
    {
        "type": "function",
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
    }
]


def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."


def get_weather(location: str, unit: str = "fahrenheit") -> str:
    """获取给定地点的当前天气信息"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})
    elif "san francisco" in location.lower():
        return json.dumps(
            {"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"}
        )
    else:
        return json.dumps({"location": location, "temperature": "unknown"})
