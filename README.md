# URL Shortener with FastAPI

## What This Does

This project is a URL shortener built using FastAPI. It allows you to convert long URLs into short, easy-to-share links and tracks how many times each short URL is accessed.

## How to Work It on Your Computer
1. Clone the repository ```
git@github.com:bigya01/AI-FELLOWSHIP-01.git
cd AI-FELLOWSHIP-01.git```
3. Create and activate a virtual environment, then install the dependencies:```python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt```
4. Run the FastAPI application using: ```uvicorn app.main:app --reload```


## Running with Docker

1. Build the Docker image:

```bash
docker build -t url-shortener .
docker run -d -p 8000:8000 url-shortener
```
The app will be available at: http://localhost:8000


