from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# import modeli żeby Alembic/SQLAlchemy je widziały
from app.models.user import User  # noqa: F401,E402
from app.models.task import Task  # noqa: F401,E402
