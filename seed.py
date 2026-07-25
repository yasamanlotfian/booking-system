from datetime import datetime

from passlib.context import CryptContext

from database import SessionLocal

from models.user import User
from models.employee import Employee
from models.event import Event
from models.appointment import Appointment


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def seed_data():

    db = SessionLocal()

    print("SEED STARTED")

    if db.query(User).first():
        print("Seed data already exists.")
        db.close()
        return

    # ---------------- Users ----------------

    admin = User(
        username="admin",
        email="admin@example.com",
        password=get_password_hash("123456"),
        role="admin"
    )

    zahra = User(
        username="zahra",
        email="zahra@example.com",
        password=get_password_hash("123456"),
        role="customer"
    )

    maryam = User(
        username="maryam",
        email="maryam@example.com",
        password=get_password_hash("123456"),
        role="customer"
    )

    fateme = User(
        username="fateme",
        email="fateme@example.com",
        password=get_password_hash("123456"),
        role="customer"
    )

    db.add_all([
        admin,
        zahra,
        maryam,
        fateme
    ])

    db.commit()

    # ---------------- Employees ----------------

    employee1 = Employee(
        name="Elham Ahmadi",
        specialty="Haircut",
        status="available"
    )

    employee2 = Employee(
        name="Negar Rezaei",
        specialty="Hair Coloring",
        status="available"
    )

    employee3 = Employee(
        name="Maryam Karimi",
        specialty="Bridal Makeup",
        status="available"
    )

    employee4 = Employee(
        name="Sara Mohammadi",
        specialty="Nail Services",
        status="available"
    )

    db.add_all([
        employee1,
        employee2,
        employee3,
        employee4
    ])

    db.commit()

    # ---------------- Events ----------------

    event1 = Event(
        title="Morning Shift",
        description="Working hours",
        employee_id=employee1.id,
        start_time=datetime(2026, 8, 1, 9, 0),
        end_time=datetime(2026, 8, 1, 15, 0)
    )

    event2 = Event(
        title="Day Off",
        description="Weekly leave",
        employee_id=employee2.id,
        start_time=datetime(2026, 8, 2, 9, 0),
        end_time=datetime(2026, 8, 2, 18, 0)
    )

    event3 = Event(
        title="Evening Shift",
        description="Working hours",
        employee_id=employee4.id,
        start_time=datetime(2026, 8, 5, 13, 0),
        end_time=datetime(2026, 8, 5, 20, 0)
    )

    db.add_all([
        event1,
        event2,
        event3
    ])

    db.commit()

    # ---------------- Appointments ----------------

    appointment1 = Appointment(
        user_id=zahra.id,
        employee_id=employee1.id,
        start_time=datetime(2026, 8, 3, 10, 0),
        end_time=datetime(2026, 8, 3, 11, 0),
        status="confirmed"
    )

    appointment2 = Appointment(
        user_id=maryam.id,
        employee_id=employee2.id,
        start_time=datetime(2026, 8, 4, 13, 0),
        end_time=datetime(2026, 8, 4, 14, 30),
        status="pending"
    )

    appointment3 = Appointment(
        user_id=fateme.id,
        employee_id=employee3.id,
        start_time=datetime(2026, 8, 5, 15, 0),
        end_time=datetime(2026, 8, 5, 16, 30),
        status="confirmed"
    )

    db.add_all([
        appointment1,
        appointment2,
        appointment3
    ])

    db.commit()

    db.close()

    print("SEED COMPLETED")


if __name__ == "__main__":
    seed_data()