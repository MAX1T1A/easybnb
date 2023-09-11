import os
import logging
from dataclasses import dataclass


@dataclass
class PostgresConfig:
    postgres_db_login: str
    postgres_db_password: str
    postgres_db_host: str
    postgres_db_port: str
    postgres_db_name: str
    echo: bool
    pool_size: int


db_config = PostgresConfig(
    postgres_db_login=os.environ["POSTGRES_DB_LOGIN"],
    postgres_db_password=os.environ["POSTGRES_DB_PASSWORD"],
    postgres_db_host=os.environ["POSTGRES_DB_HOST"],
    postgres_db_port=os.environ["POSTGRES_DB_PORT"],
    postgres_db_name=os.environ["POSTGRES_DB_NAME"],
    echo=bool(os.environ["SQLALCHEMY_ECHO"]),
    pool_size=int(os.environ["SQLALCHEMY_POOL_SIZE"]),
)


def configure_logging():
    FORMAT = "%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s"
    LEVEL = int(os.environ["LOGGING_LEVEL"])
    logging.basicConfig(level=LEVEL, format=FORMAT)
