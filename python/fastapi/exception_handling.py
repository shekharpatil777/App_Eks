from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomException)
def custom_handler(request: Request, exc: CustomException):
    return JSONResponse(status_code=418, content={"message": f"Oops! {exc.name}"})


@app.get("/error/")
def error():
    raise CustomException("Something went wrong")
