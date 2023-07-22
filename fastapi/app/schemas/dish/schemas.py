import datetime

from pydantic import BaseModel


class DishSchema(BaseModel):

    dish_id: int
    submenu_id: int

    dish_title: str
    dish_description: str
    dish_price: float
    dish_load_on: datetime.datetime

    class Config:
        from_attributes = True


class DishSchemaAdd(BaseModel):

    dish_title: str
    dish_description: str
    dish_price: float
