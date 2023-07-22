import datetime

from pydantic import BaseModel


class MenuReadByTitleSchema(BaseModel):

    title: str


class MenuAddSchema(MenuReadByTitleSchema):

    description: str


class MenuUpdateSchema(MenuAddSchema):
    ...


class MenuSchema(MenuUpdateSchema):

    menu_id: int
    load_on: datetime.datetime

    class Config:
        from_attributes = True
