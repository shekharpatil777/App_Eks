class User(BaseModel):
    username: str
    email: str


@app.get("/user/{username}", response_model=User)
def get_user(username: str):
    return {"username": username, "email": f"{username}@example.com"}