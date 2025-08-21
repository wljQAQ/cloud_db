from pydantic import BaseModel


class DBConnect(BaseModel):
    """数据库连接"""

    host: str
    port: int
    username: str
    password: str
