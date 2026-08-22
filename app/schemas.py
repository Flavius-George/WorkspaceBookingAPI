from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserRoleEnum(str, Enum):
    user = "user"
    admin = "admin"  

class ResourceTypeEnum(str, Enum):
    desk = "desk"
    room = "room"


class UserBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    role: UserRoleEnum = UserRoleEnum.user

class UserCreate(UserBase):
    password: str
    
class AdminCreate(UserCreate):
    role : UserRoleEnum =  UserRoleEnum.admin



class ResourceBase(BaseModel):
    name: str = Field(min_length= 3, max_length= 20, pattern=r"^[a-z0-9_]+$")
    type: ResourceTypeEnum 
    capacity: int = Field(ge=0)

class ResourceCreate(ResourceBase):
    pass


class BookingBase(BaseModel):
    resource_id: int
    start_time: datetime
    end_time: datetime

class BokingCreate(BookingBase):
    pass

