from fastapi import FastAPI

app = FastAPI()


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