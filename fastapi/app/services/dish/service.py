from fastapi import Depends
from typing import Annotated

from app.repositories.dish.repo import DishSqlAlchemyPgRepo


class DishSqlAlchemyPgRepoService:

    def __init__(self, repo: Annotated[DishSqlAlchemyPgRepo, Depends(DishSqlAlchemyPgRepo)]) -> None:
        self._repo: DishSqlAlchemyPgRepo = repo
