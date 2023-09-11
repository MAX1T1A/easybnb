from app.daos.v1.user_dao import UserDAO
from app.repositories.v1.user_repository import UserRepository


def provide_user_repository_stub():
    raise NotImplementedError


def provide_user_repository(dao: UserDAO) -> UserRepository:
    return UserRepository(dao)
