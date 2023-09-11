from fastapi import APIRouter, Depends

from app.models.user import UserModel
from app.repositories.v1.providers import provide_user_repository_stub
from app.repositories.v1.user_repository import UserRepository

user_router = APIRouter(prefix="/easybnb/api/v1/user", tags=["User"])


@user_router.get(
    path="/authorization/{user_id}",
    response_model=UserModel.GET.UserAuthorization.Response,
    status_code=200,
    description="Authorizes the user",
)
async def find_user_authorization(
    user_id: str, user_repository: UserRepository = Depends(dependency=provide_user_repository_stub)
) -> UserModel.GET.UserAuthorization.Response:
    return await user_repository.find_by_id(obj_id=user_id)


@user_router.post(
    path="/register",
    response_model=UserModel.POST.UserCreate.Response,
    status_code=201,
    description="User registration",
)
async def create_user(
    user_dto: UserModel.POST.UserCreate.Request,
    user_repository: UserRepository = Depends(dependency=provide_user_repository_stub),
) -> UserModel.POST.UserCreate.Response:
    return await user_repository.create_user(user_dto=user_dto)
