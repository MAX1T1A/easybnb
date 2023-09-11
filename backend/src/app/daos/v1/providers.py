from sqlalchemy.orm import sessionmaker

from app.daos.v1.user_dao import UserDAO


def provide_user_dao(session: sessionmaker) -> UserDAO:
    return UserDAO(session)
