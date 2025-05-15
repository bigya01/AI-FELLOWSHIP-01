from fastapi import FastAPI

from app.api import health
from app.core.config import settings

app = FastAPI(title=settings.app_name)


app.include_router(health.router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name} running in {settings.env} mode."
    }
