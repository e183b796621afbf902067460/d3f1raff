import datetime

from pydantic import BaseModel


class SubmenuReadByTitleSchema(BaseModel):

    title: str


class SubmenuAddSchema(SubmenuReadByTitleSchema):

    description: str


class SubmenuUpdateSchema(SubmenuAddSchema):
    ...


class SubmenuSchema(SubmenuUpdateSchema):

    submenu_id: int
    menu_id: int
    load_on: datetime.datetime

    class Config:
        from_attributes = True


class SubmenuWithDishesSchema(SubmenuSchema):

    dishes_count: int

    class Config:
        from_attributes = True
