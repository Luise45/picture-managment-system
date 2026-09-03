from fastapi import FastAPI

from database.database import Base, engine
from database import models
from routers import photos

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(photos.router)



@app.get("/")
def root():
    return {"message": "Event Photo Archive API"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/photos")
def get_photos():
    return [
        {
            "id": 1,
            "filename": "IMG_001.jpg",
            "event": "Summer Event",
        },
        {
            "id": 2,
            "filename": "IMG_002.jpg",
            "event": "Summer Event",
        },
    ]