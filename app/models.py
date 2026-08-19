
from typing import List, Optional
from datetime import datetime
from sqlalchemy import Enum, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.schemas import UserRoleEnum, ResourceTypeEnum
from sqlalchemy import Enum as SQLEnum



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] 
    role: Mapped[UserRoleEnum] = mapped_column(SQLEnum(UserRoleEnum))
    
    
    bookings: Mapped[List["Booking"]] = relationship(back_populates="user")


class Resource(Base):
    __tablename__ = "resources"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[ResourceTypeEnum] = mapped_column(SQLEnum(ResourceTypeEnum))
    capacity: Mapped[Optional[int]] 
    
   
    bookings: Mapped[List["Booking"]] = relationship(back_populates="resource")


class Booking(Base):
    __tablename__ = "bookings"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    resource_id: Mapped[int] = mapped_column(ForeignKey("resources.id"))
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    
   
    user: Mapped["User"] = relationship(back_populates="bookings")
    resource: Mapped["Resource"] = relationship(back_populates="bookings")


#async def init_models():
    #async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.create_all)

