from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.appointment import Appointment
from schemas.appointments import (
    AppointmentCreate,
    AppointmentResponse
)


router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


# Create Appointment
@router.post("/", response_model=AppointmentResponse)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    # Check appointment conflict
    existing_appointment = db.query(Appointment).filter(
        Appointment.employee_id == appointment.employee_id,
        Appointment.start_time < appointment.end_time,
        Appointment.end_time > appointment.start_time
    ).first()


    if existing_appointment:
        raise HTTPException(
            status_code=400,
            detail="Employee already has an appointment at this time"
        )


    new_appointment = Appointment(
        user_id=appointment.user_id,
        employee_id=appointment.employee_id,
        start_time=appointment.start_time,
        end_time=appointment.end_time
    )


    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)


    return new_appointment



# Get All Appointments
@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(
    db: Session = Depends(get_db)
):

    appointments = db.query(Appointment).all()

    return appointments



# Get Appointment By ID
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()


    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )


    return appointment



# Update Appointment
@router.patch("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(
    appointment_id: int,
    appointment_data: AppointmentCreate,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()


    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )


    # Check conflict except current appointment
    conflict = db.query(Appointment).filter(
        Appointment.id != appointment_id,
        Appointment.employee_id == appointment_data.employee_id,
        Appointment.start_time < appointment_data.end_time,
        Appointment.end_time > appointment_data.start_time
    ).first()


    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Employee already has another appointment at this time"
        )


    appointment.user_id = appointment_data.user_id
    appointment.employee_id = appointment_data.employee_id
    appointment.start_time = appointment_data.start_time
    appointment.end_time = appointment_data.end_time


    db.commit()
    db.refresh(appointment)


    return appointment



# Delete Appointment
@router.delete("/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()


    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )


    db.delete(appointment)
    db.commit()


    return {
        "message": "Appointment deleted successfully"
    }
