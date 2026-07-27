from typing import Optional

from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    duration: int


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    duration: Optional[int] = None


class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True