from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException , Request
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import crud, models, schemas, database

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/pincode/{pincode}", response_model=List[schemas.PincodeBase])
def read_pin(pincode: int, db: Session = Depends(get_db)):
    db_user = crud.get_pincode(db, pin_id=pincode)
    if db_user is None:
        return 'Not found'
    return db_user

@app.get("/records/{office}", response_model=List[schemas.PincodeBase])
def show_records(office:str, db: Session = Depends(get_db)):
    records = db.query(models.Pincode).filter(models.Pincode.office_name == office).all()
    return records

@app.get("/search/{query}", response_model=List[schemas.PincodeBase])
def show_records(query:Optional[str], db: Session = Depends(get_db)):
    records = db.query(models.Pincode).filter(models.Pincode.office_name.contains(query)).all()
    return records
        
   