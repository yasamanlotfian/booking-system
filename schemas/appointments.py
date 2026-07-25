from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AppointmentCreate(BaseModel):
    user_id: int
    employee_id: int
    start_time: datetime
    end_time: datetime


class AppointmentUpdate(BaseModel):
    status: Optional[str] = None


class AppointmentResponse(BaseModel):
    id: int
    user_id: int
    employee_id: int
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        from_attributes = True