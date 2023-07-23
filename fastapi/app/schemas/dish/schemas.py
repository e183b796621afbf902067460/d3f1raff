import datetime

from pydantic import BaseModel


class DishReadByTitleSchema(BaseModel):

    title: str


class DishAddSchema(DishReadByTitleSchema):

    description: str
    price: float


class DishUpdateSchema(DishAddSchema):
    ...


class DishSchema(DishUpdateSchema):

    dish_id: int
    submenu_id: int
    load_on: datetime.datetime

    class Config:
        from_attributes = True
