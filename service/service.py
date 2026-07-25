from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.appointment import Appointment
from models.room import Room
from models.service import Service

from schemas.appointments import (
    AppointmentCreate,
    AppointmentResponse
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/", response_model=AppointmentResponse)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

  service = db.query(Service).filter(
        Service.id == appointment.service_id
    ).first()


    if not service:
       raise HTTPException(
            status_code=404,
            detail="Service not found"
        )


    room = db.query(Room).filter(
        Room.id == appointment.room_id
    ).first()

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

