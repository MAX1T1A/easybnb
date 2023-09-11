from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL, Engine

from app.core.config import db_config


def construct_url(username: str, password: str, host: str, port: int, dbname: str) -> URL:
    return URL.create(
        drivername="postgresql+asyncpg",
        username=username,
        password=password,
        host=host,
        port=port,
        database=dbname,
    )


def provide_engine(url: URL | str, echo: bool, pool_size: int) -> Engine:
    return create_async_engine(url=url, echo=echo, pool_size=pool_size, future=True)


def provide_session(engine: Engine):
    return sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


def configure_engines() -> Engine:
    db_connection_uri = construct_url(
        username=db_config.postgres_db_login,
        password=db_config.postgres_db_password,
        host=db_config.postgres_db_host,
        port=db_config.postgres_db_port,
        dbname=db_config.postgres_db_name,
    )
    engine = provide_engine(
        url=db_connection_uri,
        echo=db_config.echo,
        pool_size=db_config.pool_size,
    )
    return engine
