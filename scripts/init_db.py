from app.db.session import engine
from app.db.base import Base

# import modeli, żeby metadata widziała tabele
from app.models.user import User  # noqa: F401
from app.models.task import Task  # noqa: F401

def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("OK: tables created")

if __name__ == "__main__":
    main()
