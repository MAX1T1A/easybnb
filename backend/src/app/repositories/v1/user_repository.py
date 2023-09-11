from app.daos.v1.user_dao import UserDAO
from app.models.user import UserModel
from app.repositories.v1.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, user_dao: UserDAO):
        super().__init__(dao=user_dao)

    def find_by_id(self, obj_id: str, *args, **kwargs) -> UserModel.GET.UserAuthorization.Response:
        return super().find_by_id(obj_id, *args, **kwargs)

    async def create_user(self, user_dto: UserModel.POST.UserCreate.Request) -> UserModel.POST.UserCreate.Response:
        return await self.dao.create_user(user_dto=user_dto)
