from fastapi import FastAPI, Request

app = FastAPI()


async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.url}")
    response = await call_next(request)
    return response
