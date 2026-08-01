from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ServiceBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: int = Field(..., ge=0)
    duration: int = Field(..., gt=0)


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    price: Optional[int] = Field(None, ge=0)
    duration: Optional[int] = Field(None, gt=0)


class ServiceResponse(ServiceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
