from app.services.dish.service import DishSqlAlchemyPgRepoService
from app.schemas.dish.schemas import DishAddSchema, DishUpdateSchema

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError
from typing import Annotated


router = APIRouter()


@router.post('/menus/{menu_id}/submenus/{submenu_id}/dishes', status_code=status.HTTP_200_OK)
def on_post_one(
        request: Request,
        service: Annotated[DishSqlAlchemyPgRepoService, Depends(DishSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int,
        schema: DishAddSchema
):
    try:
        dish_id: int = service.add_one(submenu_id=submenu_id, dish_title=schema.title, dish_attrs=schema.model_dump())
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id} or submenu_id {submenu_id}.')
    else:
        return dish_id


@router.get('/menus/{menu_id}/submenus/{submenu_id}/dishes', status_code=status.HTTP_200_OK)
def on_get_many(
        request: Request,
        service: Annotated[DishSqlAlchemyPgRepoService, Depends(DishSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int
):
    return service.read_all_by_submenu_id(submenu_id=submenu_id)


@router.get('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=status.HTTP_200_OK)
def on_get_one(
        request: Request,
        service: Annotated[DishSqlAlchemyPgRepoService, Depends(DishSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int,
        dish_id: int
):
    try:
        dish = service.read_one_by_id(dish_id=dish_id)
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id} or submenu_id {submenu_id}.')
    else:
        return dish


@router.patch('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=status.HTTP_200_OK)
def on_patch_one(
        request: Request,
        service: Annotated[DishSqlAlchemyPgRepoService, Depends(DishSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int,
        dish_id: int,
        schema: DishUpdateSchema
):
    try:
        dish_id = service.update_one(dish_id=dish_id, dish_attrs=schema.model_dump())
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id} or submenu_id {submenu_id}.')
    else:
        return dish_id


@router.delete('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=status.HTTP_200_OK)
def on_delete_one(
        request: Request,
        service: Annotated[DishSqlAlchemyPgRepoService, Depends(DishSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int,
        dish_id: int
):
    try:
        dish_id = service.remove_one(dish_id=dish_id)
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id} or submenu_id {submenu_id}.')
    else:
        return dish_id
