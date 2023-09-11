import re
from functools import wraps

import asyncpg
import sqlalchemy

from app.core import exceptions


def asyncpg_exc_handler(func):
    """
    Декоратор для обработки исключений psycopg2.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result

        except sqlalchemy.exc.DBAPIError as e:
            if isinstance(e.orig, asyncpg.errors.UniqueViolation):
                field = parse_field_name(r"Key \((?P<field>[\w\s,]+)\)=", str(e))

                raise exceptions.UniqueDbException(
                    field=field,
                    details=str(e),
                )

            elif isinstance(e.orig, asyncpg.errors.NotNullViolation):
                field = parse_field_name(r'column "(?P<field>\w+)" of', str(e))

                raise exceptions.NotNullDbException(field=field, details=str(e))
            elif isinstance(e.orig, asyncpg.errors.ForeignKeyViolation):
                field = foreign_key_parser(r"Key \((\w+)\)=\((.+)\)", str(e))
                raise exceptions.ForeignKeyViolation(field=field, details=str(e))

            elif isinstance(e.orig, asyncpg.errors.OperationalError):
                port_and_host = extract_host_port(str(e))
                raise exceptions.OperationalError(details=str(e), connection=port_and_host)

            elif isinstance(e.orig, asyncpg.errors.UndefinedTable):
                regex = r'relation "(?P<field>[a-zA-Z0-9_]+)" does not exist'
                field_name = parse_field_name(regex, str(e))
                raise exceptions.NotFoundException(details=str(e), message="Таблица не найдена", field=field_name)

            elif isinstance(e.orig, asyncpg.errors.InvalidTextRepresentation):
                raise exceptions.InvalidTextRepresentation(details=str(e))

            else:
                raise e

    return wrapper


def parse_field_name(regex: str, text: str) -> str:
    """
    Извлекает имя поля из сообщения об ошибке базы данных,
    используя регулярное выражение.
    """

    matches = re.search(regex, text)
    return matches.group("field") if matches else "Неизвестное поле"


def foreign_key_parser(regex: str, text: str) -> str:
    """
    Извлекает имена и значения ограничения внешнего ключа
    из сообщения об ошибке базы данных с помощью регулярного выражения.
    """

    matches = re.search(regex, text)
    return f"{matches.group(1)}={matches.group(2)}" if matches else "Неизвестное поле"


def extract_host_port(error_message: str) -> str:
    """
    Извлекает поля хоста и порта из сообщения об ошибке PostgreSQL.
    """

    host_regexes = [
        r'running on host "(.*?)"',
        r'connection to server at "(.*?)" \((?:\d{1,3}\.){3}\d{1,3}\)',
    ]
    port_regexes = [
        r"port (\d+) failed",
        r"on port (\d+)\?",
        r"TCP/IP connections on port (\d+)\?",
    ]

    for port_regex in port_regexes:
        port_matches = re.search(port_regex, error_message)
        if port_matches:
            port = port_matches.group(1)
            break
    else:
        port = "Неизвестный порт"

    for host_regex in host_regexes:
        host_matches = re.search(host_regex, error_message)
        if host_matches:
            host = host_matches.group(1)
            break
    else:
        host = "Неизвестный хост"

    return f"{host}: {port}"
