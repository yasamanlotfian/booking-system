from fastapi import FastAPI

from database import Base, engine

from models.user import User
from models.employee import Employee
from models.appointment import Appointment
from models.event import Event
from service import service

from authentication.login import router as login_router
from authentication.registration import router as registration_router
from routes import employees, appointments, events



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hair Salon Booking System API",
    description="Hair Salon Booking System using FastAPI",
    version="1.0.0"
)


# Authentication routes
app.include_router(registration_router)
app.include_router(login_router)


# Main routes
app.include_router(employees.router)
app.include_router(appointments.router)
app.include_router(events.router)
app.include_router(service.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Hair Salon Booking System API"
    }