from typing import List
from fastapi import FastAPI
from abc import ABC, abstractmethod
from fastapi_web_server.src.middleware import Middleware


class Controller(ABC):
    def __init__(
        self,
        path: str,
        method: str,
        middlewares: List[Middleware] = []
    ):
        self._app = FastAPI()
        self._path = path
        self._method = method
        self._middlewares = middlewares

        for middleware in self._middlewares:
            self._app.add_middleware(middleware)

        self._app.api_route(
            path='/',
            methods=[self._method]
        )(self.handle)

    @property
    def app(self):
        return self._app

    @property
    def path(self):
        return self._path

    @abstractmethod
    async def handle(**kwargs):
        raise NotImplemented
