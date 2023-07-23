from fastapi import Depends
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.repositories.submenu.repo import SubmenuSqlAlchemyPgRepo
from app.schemas.submenu.schemas import SubmenuSchema, SubmenuWithDishesSchema


from typing import List, Annotated


class SubmenuSqlAlchemyPgRepoService:

    def __init__(
            self,
            repo: Annotated[SubmenuSqlAlchemyPgRepo, Depends(SubmenuSqlAlchemyPgRepo)]
    ) -> None:
        self._repo: SubmenuSqlAlchemyPgRepo = repo

    def add_one(self, menu_id: int, submenu_title: str, submenu_attrs: dict) -> int:
        try:
            self._repo.select_one_by_title(model_title=submenu_title)
        except NoResultFound:
            submenu_attrs['menu_id'] = menu_id
            return self._repo.insert_one(attrs=submenu_attrs)
        else:
            raise MultipleResultsFound

    def read_one_by_id(self, submenu_id: int) -> SubmenuSchema:
        return self._repo.select_one_by_id(model_id=submenu_id)

    def read_one_by_title(self, submenu_title: str) -> SubmenuSchema:
        return self._repo.select_one_by_title(model_title=submenu_title)

    def read_all_by_menu_id(self, menu_id: int) -> List[SubmenuWithDishesSchema]:
        submenus = self._repo.select_all()
        submenus_by_menu_id = list()
        for submenu in submenus:
            if submenu.menu_id == menu_id:
                submenus_by_menu_id.append(submenu)
        return submenus_by_menu_id

    def update_one(self, submenu_id: int, submenu_attrs: dict) -> int:
        return self._repo.update_one(model_id=submenu_id, attrs=submenu_attrs)

    def remove_one(self, submenu_id: int) -> int:
        return self._repo.delete_one(model_id=submenu_id)
