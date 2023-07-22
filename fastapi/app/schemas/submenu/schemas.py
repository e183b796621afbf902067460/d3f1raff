import datetime

from pydantic import BaseModel


class SubmenuReadSchema(BaseModel):

    submenu_id: int


class SubmenuRemoveSchema(SubmenuReadSchema):
    ...


class SubmenuUpdateSchema(SubmenuReadSchema):
    ...


class SubmenuAddSchema(SubmenuReadSchema):

    submenu_title: str
    submenu_description: str


class SubmenuSchema(SubmenuAddSchema):

    menu_id: int
    submenu_load_on: datetime.datetime

    class Config:
        from_attributes = True
