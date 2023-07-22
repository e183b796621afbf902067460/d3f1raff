import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr

from app.orm.settings import base
from app.schemas.menu.schemas import MenuSchema


class menu(base):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    menu_id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    load_on: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False)

    def to_pydantic_schema(self) -> MenuSchema:
        return MenuSchema(
            menu_id=self.menu_id,
            title=self.title,
            description=self.description,
            load_on=self.load_on
        )
