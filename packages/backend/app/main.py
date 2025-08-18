import uvicorn

from typing import Union

from fastapi import FastAPI

from api import init_api

app = FastAPI()

init_api(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True, log_level="info")
