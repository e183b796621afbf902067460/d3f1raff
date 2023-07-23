from fastapi import Depends
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.repositories.dish.repo import DishSqlAlchemyPgRepo
from app.schemas.dish.schemas import DishSchema


from typing import List, Annotated


class DishSqlAlchemyPgRepoService:

    def __init__(
            self,
            repo: Annotated[DishSqlAlchemyPgRepo, Depends(DishSqlAlchemyPgRepo)]
    ) -> None:
        self._repo: DishSqlAlchemyPgRepo = repo

    def add_one(self, submenu_id: int, dish_title: str, dish_attrs: dict) -> int:
        try:
            self._repo.select_one_by_title(model_title=dish_title)
        except NoResultFound:
            dish_attrs['submenu_id'] = submenu_id
            return self._repo.insert_one(attrs=dish_attrs)
        else:
            raise MultipleResultsFound

    def read_one_by_id(self, dish_id: int) -> DishSchema:
        return self._repo.select_one_by_id(model_id=dish_id)

    def read_one_by_title(self, dish_title: str) -> DishSchema:
        return self._repo.select_one_by_title(model_title=dish_title)

    def read_all_by_submenu_id(self, submenu_id: int) -> List[DishSchema]:
        dishes = self._repo.select_all()
        dishes_by_submenu_id = list()
        for dish in dishes:
            if dish.submenu_id == submenu_id:
                dishes_by_submenu_id.append(dish)
        return dishes_by_submenu_id

    def update_one(self, dish_id: int, dish_attrs: dict) -> int:
        return self._repo.update_one(model_id=dish_id, attrs=dish_attrs)

    def remove_one(self, dish_id: int) -> int:
        return self._repo.delete_one(model_id=dish_id)
