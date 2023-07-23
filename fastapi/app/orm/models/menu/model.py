import datetime
from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column, Relationship, column_property, relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_method

from app.orm.settings import base
from app.schemas.menu.schemas import MenuSchema, MenuWithSubmenusAndDishesSchema


class menu(base):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    menu_id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    load_on: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False)

    _submenus = None

    @hybrid_method
    def _count_dishes(self) -> int:
        dishes_count = 0
        for submenu in self._submenus:
            dishes_count += len(submenu.dishes)
        return dishes_count

    @hybrid_method
    def _count_submenus(self) -> int:
        return len(self._submenus)

    def to_pydantic_schema_one(self) -> MenuSchema:
        return MenuSchema(
            menu_id=self.menu_id,
            title=self.title,
            description=self.description,
            load_on=self.load_on
        )

    def to_pydantic_schema_many(self) -> MenuWithSubmenusAndDishesSchema:

        return MenuWithSubmenusAndDishesSchema(
            menu_id=self.menu_id,
            title=self.title,
            description=self.description,
            load_on=self.load_on,
            submenus_count=self._count_submenus(),
            dishes_count=self._count_dishes()
        )
