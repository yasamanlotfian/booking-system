from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.appointment import Appointment
from models.employee import Employee
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

    employee = db.query(Employee).filter(
        Employee.id == appointment.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    new_appointment = Appointment(
        user_id=appointment.user_id,
        employee_id=appointment.employee_id,
        service_id=appointment.service_id,
        start_time=appointment.start_time,
        end_time=appointment.end_time
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment