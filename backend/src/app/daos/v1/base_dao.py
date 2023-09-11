from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

from app.core import exceptions
from app.core.decorators import asyncpg_exc_handler


class BaseDAO:
    def __init__(self, session: sessionmaker):
        self.session: sessionmaker = session
        self._model = None

    @asyncpg_exc_handler
    async def find_by_id(self, obj_id: str):
        async with self.session.begin() as transaction:
            obj = await transaction.scalar(select(self._model.id).where(self._model.id == obj_id))
            if not obj:
                raise exceptions.NotFoundException(field={"id": obj_id})

            return obj
