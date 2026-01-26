from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.user import User
from app.models.task import Task


def main() -> None:
    db = SessionLocal()
    try:
        user = db.scalar(select(User).where(User.email == "test@example.com"))
        if not user:
            user = User(email="test@example.com", hashed_password="not-a-real-hash", role="user")
            db.add(user)
            db.flush()  # dostaje id

        task = Task(title="First task", desc="Seeded task", status="todo", owner_id=user.id)
        db.add(task)

        db.commit()
        print("OK: seeded")
    finally:
        db.close()


if __name__ == "__main__":
    main()
