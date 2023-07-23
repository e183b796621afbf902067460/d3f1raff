from app.repositories.abstract import SqlAlchemyPgRepo
from app.orm import menu


class MenuSqlAlchemyPgRepo(SqlAlchemyPgRepo):
    model = menu

    @property
    def model_id(self):
        return self.model.menu_id

    @property
    def model_title(self):
        return self.model.title
