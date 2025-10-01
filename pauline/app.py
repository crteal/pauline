"""
A FastAPI application providing Pauline via hosted web experience
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

def App(**config) -> FastAPI:
    app = FastAPI()

    app.mount("/", StaticFiles(directory="./static", html=True), name="static")

    return app;
