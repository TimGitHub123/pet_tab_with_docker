from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    type = Column(String, index=True)
    created_at = Column(DateTime, index=True)


class NotDelItem(Base):
    __tablename__ = "notdelitems"

    delid = Column(Integer, index=True)
    error = Column(String, index=True)
    id = Column(Integer, primary_key=True, index=True)
