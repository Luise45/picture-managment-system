from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import SessionLocal
from database.models import Photo

router = APIRouter(
    prefix="/photos",
    tags=["photos"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_photos(db: Session = Depends(get_db)):
    return db.query(Photo).all()