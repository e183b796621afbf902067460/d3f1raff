from fastapi import Depends
from typing import Annotated

from app.repositories.submenu.repo import SubmenuSqlAlchemyPgRepo


class SubmenuSqlAlchemyPgRepoService:

    def __init__(self, repo: Annotated[SubmenuSqlAlchemyPgRepo, Depends(SubmenuSqlAlchemyPgRepo)]) -> None:
        self._repo: SubmenuSqlAlchemyPgRepo = repo

