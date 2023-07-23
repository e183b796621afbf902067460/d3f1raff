from fastapi import FastAPI

from app.settings import get_settings

from app.views.menu.view import router as menu_router
from app.views.submenu.view import router as submenu_router
from app.views.dish.view import router as dish_router


app, env = FastAPI(), get_settings()


app.include_router(router=menu_router, prefix=f'{env.API_V1}', tags=['Menu'])
app.include_router(router=submenu_router, prefix=f'{env.API_V1}', tags=['Submenu'])
app.include_router(router=dish_router, prefix=f'{env.API_V1}', tags=['Dish'])


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='__main__:app', host='0.0.0.0')
