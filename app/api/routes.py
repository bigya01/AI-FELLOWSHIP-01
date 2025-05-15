from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.api.schemas import URLRequest, URLResponse
from app.core.shortener import get_original_url, shorten_url

router = APIRouter()

BASE_URL = "http://localhost:8000"


@router.post("/shorten", response_model=URLResponse)
def create_short_url(payload: URLRequest):
    code = shorten_url(payload.url)
    return {"short_url": f"{BASE_URL}/{code}"}


@router.get("/{code}")
def redirect_to_original(code: str):
    original_url = get_original_url(code)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(original_url)
