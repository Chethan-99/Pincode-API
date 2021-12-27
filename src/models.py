from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Pincode(Base):
    __tablename__ = 'Pincodes'
    id = Column(Integer, primary_key=True, index=True)
    circle_name = Column(String(50))
    region_name = Column(String(50))
    division = Column(String(50))
    office_name = Column(String(50))
    pincode = Column(Integer)
    office_type = Column(String(5))
    delivery = Column(String(20))
    district = Column(String(50))
    state_name = Column(String(50))
