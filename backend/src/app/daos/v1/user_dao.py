import random

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert

from app.core.decorators import asyncpg_exc_handler
from app.daos.v1.base_dao import BaseDAO
from app.dblayer.tables import User
from app.models.user import UserModel


class UserDAO(BaseDAO):
    def __init__(self, session: sessionmaker):
        super().__init__(session=session)
        self._model: User = User

    @asyncpg_exc_handler
    async def create_user(self, user_dto: UserModel.POST.UserCreate.Request) -> UserModel.POST.UserCreate.Response:
        async with self.session.begin() as transaction:
            res = await transaction.execute(
                insert(self._model)
                .values(**user_dto.model_dump(exclude={"id"}), id=random.randint(100, 10000000))
                .returning(self._model.name, self._model.surname)
            )
            print(res.one())
            return res
