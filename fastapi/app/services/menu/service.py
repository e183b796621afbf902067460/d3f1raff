from fastapi import Depends
from sqlalchemy.orm.exc import NoResultFound

from app.repositories.menu.repo import MenuSqlAlchemyPgRepo
from app.schemas.menu.schemas import MenuSchema, MenuWithSubmenusAndDishesSchema


from typing import List, Annotated


class MenuSqlAlchemyPgRepoService:

    def __init__(self, repo: Annotated[MenuSqlAlchemyPgRepo, Depends(MenuSqlAlchemyPgRepo)]) -> None:
        self._repo: MenuSqlAlchemyPgRepo = repo

    def add_one(self, menu_title: str, menu_attrs: dict) -> int:
        try:
            self._repo.select_one_by_title(model_title=menu_title)
        except NoResultFound:
            return self._repo.insert_one(attrs=menu_attrs)

    def read_one_by_id(self, menu_id: int) -> MenuSchema:
        return self._repo.select_one_by_id(model_id=menu_id)

    def read_one_by_title(self, menu_title: str) -> MenuSchema:
        return self._repo.select_one_by_title(model_title=menu_title)

    def read_all(self) -> List[MenuWithSubmenusAndDishesSchema]:
        return self._repo.select_all()

    def update_one(self, menu_id: int, menu_attrs: dict) -> int:
        return self._repo.update_one(model_id=menu_id, attrs=menu_attrs)

    def remove_one(self, menu_id: int) -> int:
        return self._repo.delete_one(model_id=menu_id)
