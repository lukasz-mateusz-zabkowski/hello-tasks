from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.get("/tasks")
def list_tasks() -> list[dict]:
    return [
        {"id": 1, "title": "Learn FastAPI", "completed": False},
        {"id": 2, "title": "Connect PostgreSQL later", "completed": False},
    ]
