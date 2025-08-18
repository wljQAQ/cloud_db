from fastapi import FastAPI

from .routes import init_all_routes


def init_api(app: FastAPI) -> None:
    init_all_routes(app)
