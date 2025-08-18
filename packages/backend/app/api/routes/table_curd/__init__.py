from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["table curd"])

from . import controller
