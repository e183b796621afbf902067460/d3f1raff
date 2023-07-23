import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr

from app.orm.settings import base
from app.schemas.dish.schemas import DishSchema


class dish(base):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    dish_id: Mapped[int] = mapped_column(primary_key=True)
    submenu_id: Mapped[int] = mapped_column(ForeignKey('submenu.submenu_id', ondelete='CASCADE'))

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    load_on: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False)

    _submenu = None

    def to_pydantic_schema_one(self) -> DishSchema:
        return DishSchema(
            dish_id=self.dish_id,
            submenu_id=self.submenu_id,
            title=self.title,
            description=self.description,
            price=self.price,
            load_on=self.load_on
        )

    def to_pydantic_schema_many(self) -> DishSchema:
        return self.to_pydantic_schema_one()
