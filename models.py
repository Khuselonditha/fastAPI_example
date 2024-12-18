# imports
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum

# Enum class for Gender
class Gender(str, Enum):
    male = "male"
    female = "female"

# Define the model of our user
class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender 