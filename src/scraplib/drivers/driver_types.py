from pydantic import BaseModel
from enum import Enum

class EGender(Enum):
    male = "male"
    female = "female"
    

class FriendFilter(BaseModel):
    gender: EGender

