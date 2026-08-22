import schemas
import models
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import DateTime, select, insert

async def create_user(db: AsyncSession, user_data:schemas.UserCreate):
    new_user = models.User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email = user_data.email,
        hashed_password = user_data.password,
        role = user_data.role
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

async def get_user_by_email(db: AsyncSession, user_email: str):
    stmt = select(models.User).where(models.User.email == user_email)
    result = await db.execute(stmt)
    found_user = result.scalar_one_or_none()
    return found_user

async def check_overlapping_booking(db: AsyncSession, resource_id:int, activity_beginning: DateTime, activity_end: DateTime):
    stmt = select(models.Booking.id, models.Booking.resource_id, models.Booking.start_time, models.Booking.end_time).where(resource_id==models.Booking.resource_id, activity_beginning<models.Booking.end_time, activity_end>models.Booking.start_time)
    result = await db.execute(stmt)
    overlapping_booking = result.first()

    if overlapping_booking:
        return True

    return False

    