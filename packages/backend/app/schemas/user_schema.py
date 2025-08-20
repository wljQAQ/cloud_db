from pydantic import BaseModel


# 这个文件专门存放与用户相关的Pydantic模型
# 这些模型定义了API的数据结构 (Data Transfer Objects)


class UserSchema(BaseModel):
    """用户数据的基础模型"""

    id: int
    username: str

    # Pydantic v2 推荐使用 model_config 来配置ORM模式等
    # 这里暂时不需要，但保留一个示例
    class Config:
        from_attributes = True
