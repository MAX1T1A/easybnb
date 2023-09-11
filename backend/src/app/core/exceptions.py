from dataclasses import dataclass


class ApiException(Exception):
    pass


@dataclass
class BadRequestException(ApiException):
    message: str = "Неверные данные запроса"
    code: str = "B001"
    details: list | str | None = None


@dataclass
class NoPermissionException(ApiException):
    message: str = "Нет прав на выполнение операции"
    code: str = "P001"
    details: str | None = None


@dataclass
class DbException(ApiException):
    message: str
    field: str | None = None
    code: str = "D001"
    details: str | None = None


@dataclass
class NotNullDbException(DbException):
    code: str = "D002"
    message: str = "Указан null, но поле не может быть null"


@dataclass
class UniqueDbException(DbException):
    code: str = "D003"
    message: str = "Объект уже существует или дублирование по полю"


@dataclass
class ForeignKeyViolation(DbException):
    code: str = "D004"
    message: str = (
        "Добавление данного объекта невозможно, "
        "так как он ссылается на несуществующий объект. "
        "Проверьте его наличие в базе данных"
    )


@dataclass
class NotFoundException(ApiException):
    message: str = "Объект не найден"
    code: str = "D005"
    field: str | dict | None = None
    details: str | None = None


@dataclass
class OperationalError(DbException):
    code: str = "D006"
    message: str = "Не удалось подключиться к базе данных. " "Проверьте настройки подключения"
    connection: str = ""


@dataclass
class InvalidTextRepresentation(DbException):
    code: str = "D007"
    message: str = "Неверное значение Enum"
    field: str | None = None


@dataclass
class UnexpectedServerException(ApiException):
    message: str = "Непредвиденная ошибка сервера"
    code: str = "S001"
    details: str | None = None
