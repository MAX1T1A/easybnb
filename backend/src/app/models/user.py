from pydantic import BaseModel


class UserModel:
    class GET:
        class UserAuthorization:
            class Request(BaseModel):
                pass

            class Response(BaseModel):
                id: int

        class UserCreate(BaseModel):
            name: str
            surname: str

    class POST:
        class UserCreate:
            class Base(BaseModel):
                name: str | None
                surname: str | None

            class Request(Base):
                id: int
                phone_number: str

            class Response(Base):
                pass
