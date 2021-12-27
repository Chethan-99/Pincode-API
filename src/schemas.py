from typing import List, Optional

from pydantic import BaseModel


class PincodeBase(BaseModel):
    id: Optional[int]
    circle_name: Optional[str]
    region_name: Optional[str]
    division: Optional[str]
    office_name: Optional[str]
    pincode: Optional[int]
    office_type: Optional[str]
    delivery: Optional[str]
    district: Optional[str]
    state_name: Optional[str]

    class Config:
        orm_mode = True
    

class PincodeCreate(PincodeBase):
    pass


class Pincode(PincodeBase):
    id: int

    class Config:
        orm_mode = True
