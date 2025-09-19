from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
