from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, DeclarativeBase

from pydantic_settings import BaseSettings


class base(DeclarativeBase):
    ...


class _PgSettings(BaseSettings):

    @staticmethod
    def _uri() -> str:
        return "postgresql://postgres:postgres@postgres/postgres"

    @classmethod
    def _engine(cls) -> Engine:
        return create_engine(cls._uri())

    @classmethod
    def session(cls) -> Session:
        return Session(bind=cls._engine())


def get_session() -> Session:
    with _PgSettings.session() as s:
        yield s
