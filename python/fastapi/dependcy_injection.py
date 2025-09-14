from fastapi import Depends

def common_params(q: str | None = None, limit: int = 10):
    return {"q": q, "limit": limit}

