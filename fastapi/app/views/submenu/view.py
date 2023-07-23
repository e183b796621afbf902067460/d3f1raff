from app.services.submenu.service import SubmenuSqlAlchemyPgRepoService
from app.schemas.submenu.schemas import SubmenuAddSchema, SubmenuUpdateSchema

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError
from typing import Annotated


router = APIRouter()


@router.post('/menus/{menu_id}/submenus', status_code=status.HTTP_200_OK)
def on_post_one(
        request: Request,
        service: Annotated[SubmenuSqlAlchemyPgRepoService, Depends(SubmenuSqlAlchemyPgRepoService)],
        menu_id: int,
        schema: SubmenuAddSchema
):
    try:
        submenu_id: int = service.add_one(menu_id=menu_id, submenu_title=schema.title, submenu_attrs=schema.model_dump())
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id}.')
    else:
        return submenu_id


@router.get('/menus/{menu_id}/submenus', status_code=status.HTTP_200_OK)
def on_get_many(
        request: Request,
        service: Annotated[SubmenuSqlAlchemyPgRepoService, Depends(SubmenuSqlAlchemyPgRepoService)],
        menu_id: int
):
    return service.read_all_by_menu_id(menu_id=menu_id)


@router.get('/menus/{menu_id}/submenus/{submenu_id}', status_code=status.HTTP_200_OK)
def on_get_one(
        request: Request,
        service: Annotated[SubmenuSqlAlchemyPgRepoService, Depends(SubmenuSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int
):
    try:
        submenu = service.read_one_by_id(submenu_id=submenu_id)
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id}.')
    else:
        return submenu


@router.patch('/menus/{menu_id}/submenus/{submenu_id}', status_code=status.HTTP_200_OK)
def on_patch_one(
        request: Request,
        service: Annotated[SubmenuSqlAlchemyPgRepoService, Depends(SubmenuSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int,
        schema: SubmenuUpdateSchema
):
    try:
        submenu_id = service.update_one(submenu_id=submenu_id, submenu_attrs=schema.model_dump())
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id}.')
    else:
        return submenu_id


@router.delete('/menus/{menu_id}/submenus/{submenu_id}', status_code=status.HTTP_200_OK)
def on_delete_one(
        request: Request,
        service: Annotated[SubmenuSqlAlchemyPgRepoService, Depends(SubmenuSqlAlchemyPgRepoService)],
        menu_id: int,
        submenu_id: int
):
    try:
        submenu_id = service.remove_one(submenu_id=submenu_id)
    except NoResultFound:
        ...
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No such menu_id {menu_id}')
    else:
        return submenu_id
