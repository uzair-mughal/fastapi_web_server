import uvicorn
from typing import List
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from gunicorn.app.base import BaseApplication
from fastapi_web_server.src.api_doc import ApiDoc
from fastapi_web_server.src.config import Config
from fastapi_web_server.src.controller import Controller
from fastapi_web_server.src.exception_handler import ExceptionHandler
from fastapi_web_server.src.middleware import Middleware


class UnicornServer:
    def __init__(
        self,
        config: Config = Config(),
        controllers: List[Controller] = [],
        middlewares: List[Middleware] = [],
        exception_handler: ExceptionHandler = None,
        api_doc: ApiDoc = ApiDoc(),
    ):
        self._application = FastAPI()
        self._controllers = controllers
        self._exception_handler = exception_handler
        self._middlewares = middlewares
        self._api_doc = api_doc
        self._routes = []

        self.options = config.to_dict()

        super().__init__()

        for controller in self._controllers:
            for middleware in self._middlewares:
                controller.app.add_middleware(middleware)

            if self._exception_handler:
                controller.app.exception_handler(Exception)(self._exception_handler.handle)

            self._application.mount(controller.path, controller.app)
            self._routes.extend(controller.app.routes)

        self._application.openapi = lambda: get_openapi(routes=self._routes, **self._api_doc.to_dict())

    def start(self):
        uvicorn.run(self._application, **self.options)
