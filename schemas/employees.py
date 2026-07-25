from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    specialty: str


class EmployeeUpdate(BaseModel):
    name: str
    specialty: str
    status: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    specialty: str
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )