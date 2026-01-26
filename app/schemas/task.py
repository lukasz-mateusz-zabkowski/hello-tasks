from pydantic import BaseModel, Field
from typing import Optional, Literal


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

    class Config:
        from_attributes = True  # Pydantic v2 (z ORM)

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["todo", "doing", "done"]] = None
