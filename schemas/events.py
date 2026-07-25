from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    employee_id: int
    start_time: datetime
    end_time: datetime


class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    employee_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True