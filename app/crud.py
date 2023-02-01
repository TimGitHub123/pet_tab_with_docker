import datetime
from sqlalchemy.orm import Session
from . import models, schemas


def get_items(db: Session, limit: int = 20):
    return db.query(models.Item).limit(limit).all()


def create_pets_table_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, age=item.age, type=item.type, created_at=datetime.datetime.now())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_not_del_items(db: Session):
    return db.query(models.NotDelItem).all()


def create_not_del_pet_item(db: Session, ind: int):
    db_delitem = models.NotDelItem(delid=ind, error="Pet with the matching ID was not found")
    db.add(db_delitem)
    db.commit()
    db.refresh(db_delitem)
    return
