import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr

from app.orm.settings import base
from app.schemas.submenu.schemas import SubmenuSchema


class submenu(base):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    submenu_id: Mapped[int] = mapped_column(primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey('menu.menu_id'))

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    load_on: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False)

    def to_pydantic_schema(self) -> SubmenuSchema:
        return SubmenuSchema(
            submenu_id=self.submenu_id,
            menu_id=self.menu_id,
            title=self.title,
            description=self.description,
            load_on=self.load_on
        )
