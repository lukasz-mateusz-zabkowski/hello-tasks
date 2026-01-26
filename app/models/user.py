from sqlalchemy import Column, Integer, String
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)


# from app.db.session import Base

# from datetime import datetime

# from sqlalchemy import String, DateTime
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from app.db.base import Base

# class User(Base):
#    __tablename__ = "users"
#
#    id: Mapped[int] = mapped_column(primary_key=True)
#    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
#    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
#    role: Mapped[str] = mapped_column(String(50), nullable=False, default="user")
#    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

#    tasks = relationship("Task", back_populates="owner")
