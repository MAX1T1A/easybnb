from sqlalchemy import String, DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.dblayer.enums import Status


# Создание базового класса
class Base(DeclarativeBase):
    pass


class TimeStampMixin(Base):
    __abstract__ = True

    # By Create
    created_by: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    # Updated
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    # Deleted
    deleted_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)


class User(TimeStampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), nullable=False)
    status: Mapped[Status] = mapped_column(server_default=Status.UNVERIFIED)

    created_by = None
