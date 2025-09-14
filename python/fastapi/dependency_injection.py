from fastapi import Depends

def common_params(q: str | None = None, limit: int = 10):
    return {"q": q, "limit": limit}

@app.get("/search/")
def search(params: dict = Depends(common_params)):
    return params

