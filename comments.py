from fastapi import APIRouter, Path
from model import Comments

comments_router = APIRouter()

comments_list = []

@comments_router.get("/comments")
async def comments() -> dict:
    return {"msg": "Comment received", "comment": comments_list}
 