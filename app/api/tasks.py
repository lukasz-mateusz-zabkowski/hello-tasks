from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
import app.db.base  # noqa: F401

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

# 🔹 ROUTER MUSI BYĆ NA GÓRZE
router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =====================
# LIST TASKS
# =====================
@router.get("", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


# =====================
# CREATE TASK
# =====================
@router.post("", response_model=TaskRead)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        title=payload.title,
        description=payload.description,
        status="todo",
        owner_id=1,  # tymczasowo
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


# =====================
# GET TASK BY ID
# =====================
@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# =====================
# UPDATE TASK
# =====================
@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        task.title = payload.title
    if payload.description is not None:
        task.description = payload.description
    if payload.status is not None:
        task.status = payload.status

    db.commit()
    db.refresh(task)
    return task


# =====================
# DELETE TASK
# =====================
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return None
