from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    specialty = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="available"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    appointments = relationship(
        "Appointment",
        back_populates="employee"
    )

    events = relationship(
        "Event",
        back_populates="employee"
    )