from datetime import datetime

from sqlalchemy import String, DateTime, Date, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(
        String(
            100,
        ),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(
            100,
        ),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(
            100,
        ),
        nullable=False,
        unique=True,
    )
    phone: Mapped[str] = mapped_column(
        String(
            20,
        ),
        nullable=True,
    )
    birthday: Mapped[datetime] = mapped_column(
        Date,
        nullable=False,
    )
    optional_data: Mapped[str] = mapped_column(
        String(
            300,
        ),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now, onupdate=func.now
    )
