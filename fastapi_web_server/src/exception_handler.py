from abc import ABC, abstractmethod
from fastapi import Request, Response


class ExceptionHandler(ABC):
    @abstractmethod
    async def handle(request: Request, ex: Exception) -> Response:
        raise NotImplementedError()
