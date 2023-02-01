from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pet/items/", response_model=schemas.Item)
def create_item_for_table(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_pets_table_item(db=db, item=item)


@app.get("/items/")
def read_items(limit: int = 20, db: Session = Depends(get_db)):
    items = crud.get_items(db, limit=limit)
    count = 0
    for i in items:
        if i:
            count += 1
    return {"count": count, "items": items}


@app.delete("/items/")
def delete_item(item: schemas.DeleteRequest, db: Session = Depends(get_db)):
    iterator = 1
    if db.get(models.NotDelItem, iterator):
        while db.get(models.NotDelItem, iterator):
            deleted = db.get(models.NotDelItem, iterator)
            db.delete(deleted)
            db.commit()
            iterator += 1
    del_count = 0
    for i in item.ids:
        deleted = db.get(models.Item, i)
        if deleted:
            db.delete(deleted)
            db.commit()
            del_count += 1
            continue
        crud.create_not_del_pet_item(db=db, ind=i)
    if crud.get_not_del_items(db):
        return {"deleted:": del_count, "errors": crud.get_not_del_items(db)}
    return {"deleted:": del_count, "errors": "No errors exists!"}
