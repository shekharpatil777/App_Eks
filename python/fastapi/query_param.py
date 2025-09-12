from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, q: Union[str, None] = None):
    return {"skip": skip, "limit": limit, "q": q}