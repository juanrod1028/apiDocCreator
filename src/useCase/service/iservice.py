from abc import ABC, abstractmethod
from src.useCase.models.request import Request
from src.useCase.models.response import Response


class IService(ABC):
    @abstractmethod
    def create_apidoc(self, request: Request) -> Response:
        pass
