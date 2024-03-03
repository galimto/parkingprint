from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from domain.park import park_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",  # 또는 "http://localhost:5173"
    "http://localhost:5173",
    "http://localhost:5172",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보23  "}


app.include_router(park_router.router, tags=["sss", "ddd"])
