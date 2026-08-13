
from typing import List, Optional
from datetime import datetime
from sqlalchemy import Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] 
    role: Mapped[str] = mapped_column(Enum("admin", "user", name="enum_role"))
    
    
    bookings: Mapped[List["Booking"]] = relationship(back_populates="user")


class Resource(Base):
    __tablename__ = "resources"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str] = mapped_column(Enum("desk", "room", name="enum_type"))
    capacity: Mapped[Optional[int]] 
    
   
    bookings: Mapped[List["Booking"]] = relationship(back_populates="resource")


class Booking(Base):
    __tablename__ = "bookings"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    resource_id: Mapped[int] = mapped_column(ForeignKey("resources.id"))
    start_time: Mapped[datetime] = mapped_column(TIMESTAMP)
    end_time: Mapped[datetime] = mapped_column(TIMESTAMP)
    
   
    user: Mapped["User"] = relationship(back_populates="bookings")
    resource: Mapped["Resource"] = relationship(back_populates="bookings")

user="db_user"
password="db_password"
port=""
db="db_name"

#engine=create_engine(f"postgresql+psycopg2://{$user}:{$password}@localhost:port/{$dbname}")