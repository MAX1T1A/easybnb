from fastapi import FastAPI
from sqlalchemy.engine import Engine

from app.core.config import configure_logging
from app.core.exc_handling import configure_exceptions_handlers
from app.daos.v1.providers import provide_user_dao
from app.dblayer.connection import provide_session, configure_engines
from app.handlers.v1.user import user_router
from app.repositories.v1.providers import provide_user_repository, provide_user_repository_stub

application = FastAPI(
    title="Easy Bed and Breakfast Service",
    docs_url="/easybnb/api/v1/docs",
    redoc_url="/easybnb/api/v1/redoc",
    openapi_url="/easybnb/api/v1/openapi.json",
)


def setup_di(app: FastAPI, engine: Engine) -> None:
    session = provide_session(engine=engine)

    user_dao = provide_user_dao(session=session)

    user_repository = lambda: provide_user_repository(dao=user_dao)

    app.dependency_overrides[provide_user_repository_stub] = user_repository


def build_app(engine: Engine) -> FastAPI:
    setup_di(app=application, engine=engine)
    application.include_router(router=user_router)

    return application


def get_app() -> FastAPI:
    configure_logging()
    configure_exceptions_handlers(application)
    engine = configure_engines()

    return build_app(engine=engine)
