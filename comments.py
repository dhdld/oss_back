from fastapi import APIRouter, Path
from model import Comment

comments_router = APIRouter()

comments_list = []

@comments_router.get("/comments")
async def comments() -> dict:
    return {"comments": comments_list}

@comments_router.post("/comments")
async def add_comment(comment: Comment) -> dict:
    comment.id = len(comments_list) + 1
    comments_list.append(comment)
    return {"msg": "comment added successfully"}

@comments_router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int = Path(..., title="the ID of comment to delete")) -> dict:
    for i, comment in enumerate(comments_list):
        if comment.id == comment_id:
            del comments_list[i]
            return {"msg": f"comment {comment_id} deleted successfully"}
        return {"msg": f"comment {comment_id} not found"}