from sqlalchemy import Column, Integer, String

from .database import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    onedrive_item_id = Column(String, unique=True)
    event_name = Column(String)