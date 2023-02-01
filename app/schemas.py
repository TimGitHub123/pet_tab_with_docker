import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    age: int
    type: str
    created_at: datetime.datetime


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class NotDelItemBase(BaseModel):
    delid: int | None = None
    error: str | None = None
    id: int | None = None


class NotDelItemCreate(NotDelItemBase):
    pass


class NotDelItem(NotDelItemBase):
    class Config:
        orm_mode = True


class DeleteRequest(BaseModel):
    ids: list[int]
