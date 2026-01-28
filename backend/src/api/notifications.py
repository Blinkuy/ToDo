from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import NotificationRepository
from src.database.deps import get_session

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/")
async def get_notifications(
    session: AsyncSession = Depends(get_session)
):
    notifications = await NotificationRepository.get_all(session=session)

    return notifications
