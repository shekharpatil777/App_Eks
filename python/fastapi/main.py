from fastapi import FastAPI
from routers import items # Assuming routers is a package and items.py is a module within it

app = FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}