from fastapi import APIRouter

from packages.backend.app.schemas.database_schema import DBConnect


router = APIRouter(prefix="/db", tags=["db"])


@router.post("/connect")
def connect(self, connect_params: DBConnect):
    "连接数据库"
