from abc import ABC, abstractmethod
from typing import Annotated

from app.orm.settings import get_session

from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from fastapi import Depends


# TODO https://python.plainenglish.io/design-patterns-in-python-repository-pattern-1c2e5070a01c
class iRepo(ABC):

    @abstractmethod
    def insert_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def select_one_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def select_one_by_title(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def select_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self, *args, **kwargs):
        raise NotImplementedError


class SqlAlchemyPgRepo(iRepo):
    model = None

    def __init__(self, session: Annotated[Session, Depends(get_session)]) -> None:
        self._session: Session = session

    @property
    @abstractmethod
    def model_id(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def model_title(self):
        raise NotImplementedError

    def insert_one(self, attrs: dict) -> int:
        with self._session as session:
            sql = insert(self.model).values(**attrs).returning(self.model_id)
            model_id = session.execute(sql)

            session.commit()

            return model_id.scalar_one()

    def select_one_by_id(self, model_id: int):
        with self._session as session:
            sql = select(self.model).where(self.model_id == model_id)
            orm_model = session.execute(sql).one()

            return orm_model[0].to_pydantic_schema_one()

    def select_one_by_title(self, model_title: str):
        with self._session as session:
            sql = select(self.model).where(self.model_title == model_title)
            orm_model = session.execute(sql).one()

            return orm_model[0].to_pydantic_schema_one()

    def select_all(self):
        with self._session as session:
            sql = select(self.model)
            orm_models = session.execute(sql).all()

            return [orm_model[0].to_pydantic_schema_many() for orm_model in orm_models]

    def update_one(self, model_id: int, attrs: dict) -> int:
        with self._session as session:
            sql = update(self.model).where(self.model_id == model_id).values(**attrs).returning(self.model_id)
            model_id = session.execute(sql)

            session.commit()

            return model_id.scalar_one()

    def delete_one(self, model_id: int) -> int:
        with self._session as session:
            sql = delete(self.model).where(self.model_id == model_id).returning(self.model_id)
            model_id = session.execute(sql)

            session.commit()

            return model_id.scalar_one()
