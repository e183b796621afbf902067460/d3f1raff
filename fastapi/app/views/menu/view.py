from app.services.menu.service import MenuSqlAlchemyPgRepoService
from app.schemas.menu.schemas import MenuAddSchema, MenuUpdateSchema

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.exc import NoResultFound
from typing import Annotated


router = APIRouter()


@router.post('/menus', status_code=status.HTTP_200_OK)
def on_post_one(
        request: Request,
        service: Annotated[MenuSqlAlchemyPgRepoService, Depends(MenuSqlAlchemyPgRepoService)],
        schema: MenuAddSchema
):
    return service.add_one(menu_title=schema.title, menu_attrs=schema.model_dump())


@router.get('/menus', status_code=status.HTTP_200_OK)
def on_get_many(
        request: Request,
        service: Annotated[MenuSqlAlchemyPgRepoService, Depends(MenuSqlAlchemyPgRepoService)]
):
    return service.read_all()


@router.get('/menus/{menu_id}', status_code=status.HTTP_200_OK)
def on_get_one(
        request: Request,
        service: Annotated[MenuSqlAlchemyPgRepoService, Depends(MenuSqlAlchemyPgRepoService)],
        menu_id: int
):
    try:
        menu = service.read_one_by_id(menu_id=menu_id)
    except NoResultFound:
        ...
    else:
        return menu


@router.patch('/menus/{menu_id}', status_code=status.HTTP_200_OK)
def on_patch_one(
        request: Request,
        service: Annotated[MenuSqlAlchemyPgRepoService, Depends(MenuSqlAlchemyPgRepoService)],
        menu_id: int,
        schema: MenuUpdateSchema
):
    try:
        menu_id = service.update_one(menu_id=menu_id, menu_attrs=schema.model_dump())
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return menu_id


@router.delete('/menus/{menu_id}', status_code=status.HTTP_200_OK)
def on_delete_one(
        request: Request,
        service: Annotated[MenuSqlAlchemyPgRepoService, Depends(MenuSqlAlchemyPgRepoService)],
        menu_id: int
):
    try:
        menu_id = service.remove_one(menu_id=menu_id)
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return menu_id
