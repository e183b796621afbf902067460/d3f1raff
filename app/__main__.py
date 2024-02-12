from fastapi import FastAPI

from app.containers.application import ApplicationContainer
from app.views.quickswap_v3.view import lifespan


container = ApplicationContainer()
container.wire(modules=[__name__])

app = FastAPI(lifespan=lifespan)
app.container = container


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="__main__:app", host="0.0.0.0")
