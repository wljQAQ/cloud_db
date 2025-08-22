from fastapi import APIRouter, Depends

from schemas.database_schema import DBConnect

from services.database_service import DatabaseService, database_service


router = APIRouter(prefix="/db", tags=["db"])


@router.post("/connect")
def connect(
    connect_params: DBConnect,
    db_service: DatabaseService = Depends(lambda: database_service),
):
    "连接数据库"
    db_service.connect_test(connect_params)
