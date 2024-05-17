from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from comments import comments_router

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome oss hw backend home"}

app.include_router(comments_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)