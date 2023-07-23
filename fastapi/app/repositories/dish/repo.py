from app.repositories.abstract import SqlAlchemyPgRepo
from app.orm import dish


class DishSqlAlchemyPgRepo(SqlAlchemyPgRepo):
    model = dish

    @property
    def model_id(self):
        return self.model.dish_id

    @property
    def model_title(self):
        return self.model.title
