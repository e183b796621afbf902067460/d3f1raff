from app.repositories.abstract import SqlAlchemyPgRepo
from app.orm import submenu


class SubmenuSqlAlchemyPgRepo(SqlAlchemyPgRepo):
    model = submenu

    @property
    def model_id(self):
        return self.model.submenu_id

    @property
    def model_title(self):
        return self.model.title
