from pydantic import BaseModel

class Comments(BaseModel):
    id: int
    name: str
    contents: str