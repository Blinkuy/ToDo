from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import UserRepository
from src.database.deps import get_session
from src.schemas.user import UserCreateRequest, UserResponse

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/get_all", response_model=list[UserResponse])
async def get_users(
    session: AsyncSession = Depends(get_session)
):
    users = await UserRepository.get_all(session=session)

    return users


@router.post("/add", response_model=UserResponse)
async def add_user(
    user: UserCreateRequest,
    session: AsyncSession = Depends(get_session)
):
    user = await UserRepository.add_one(
        session=session,
        user_data=user
    )

    return user
