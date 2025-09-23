# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Assume db_session, models, and schemas are defined elsewhere
# from . import models, schemas
# from .database import SessionLocal, engine



@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    This endpoint depends on a database session.
    FastAPI will handle creating it via get_db() before the request
    and closing it after the request is finished.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item