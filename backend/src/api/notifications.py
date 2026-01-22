from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import NotificationRepository
from src.database.deps import get_session

router = APIRouter(prefix="/notification", tags=["Notification"])


@router.get("/get_all")
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await NotificationRepository.get_all(session=session)

    return users
