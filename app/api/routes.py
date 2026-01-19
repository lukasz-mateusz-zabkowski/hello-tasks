from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["tasks"])


class HealthResponse(BaseModel):
    status: str


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


@router.get(
    "/health",
    summary="Health check",
    description="Prosty endpoint do sprawdzenia czy API działa.",
    response_model=HealthResponse,
)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get(
    "/tasks",
    summary="List tasks",
    description="Zwraca listę zadań (na razie na sztywno, bez bazy).",
    response_model=list[TaskResponse],
)
def list_tasks() -> list[TaskResponse]:
    return [
        TaskResponse(id=1, title="Learn FastAPI", completed=False),
        TaskResponse(id=2, title="Connect PostgreSQL later", completed=False),
    ]
