from fastapi import FastAPI
from app.api import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to the URL Shortener"}
