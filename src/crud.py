from sqlalchemy.orm import Session
import models, schemas


def get_pincode(db: Session, pin_id: int):
    return db.query(models.Pincode).filter(models.Pincode.pincode == pin_id).all()


def create_user_item(db: Session, item: schemas.PincodeCreate, id: int):
    db_item = models.Pincode(**item.dict(), id=id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item