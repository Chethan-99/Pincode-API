
import csv

import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("Pincode.csv", "r") as f:
    csv_reader = csv.DictReader(f)


    for row in csv_reader:
        print(row["Office Name"])
        db_record = models.Pincode(
            circle_name=row["Circle Name"],
            region_name=row["Region Name"],
            division=row["Division Name"],
            office_name=row["Office Name"],
            pincode=row["Pincode"],
            office_type=row["OfficeType"],
            delivery=row["Delivery"],
            district=row["District"],
            state_name=row["StateName"],
        )
        db.add(db_record)
  
    db.commit()
print("done")
db.close()