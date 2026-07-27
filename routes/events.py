from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.event import Event
from schemas.events import EventCreate, EventResponse

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


# Create Event
@router.post("/", response_model=EventResponse)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):
    new_event = Event(
        title=event.title,
        description=event.description,
        employee_id=event.employee_id,
        start_time=event.start_time,
        end_time=event.end_time
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


# Get All Events
@router.get("/", response_model=list[EventResponse])
def get_events(
    db: Session = Depends(get_db)
):
    return db.query(Event).all()


# Get Event By ID
@router.get("/{event_id}", response_model=EventResponse)
def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


# Update Event
@router.put("/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    event_data: EventCreate,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    event.title = event_data.title
    event.description = event_data.description
    event.employee_id = event_data.employee_id
    event.start_time = event_data.start_time
    event.end_time = event_data.end_time

    db.commit()
    db.refresh(event)

    return event


# Delete Event
@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    db.delete(event)
    db.commit()

    return {
        "message": "Event deleted successfully"
    }
