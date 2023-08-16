from abc import abstractmethod
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class Middleware(BaseHTTPMiddleware):
    @abstractmethod
    async def dispatch(request: Request, call_next) -> Response:
        raise NotImplementedError()
