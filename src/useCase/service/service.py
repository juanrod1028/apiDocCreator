from fastapi.responses import JSONResponse
from src.useCase.service.iservice import IService
from src.useCase.models.request import Request
from src.useCase.utils.response_builder import ResponseBuilder


class Service(IService):
    def create_apidoc(self, request: Request) -> JSONResponse:
        if request.method == "post":
            return ResponseBuilder.request_successfull(request.body)
        if request.method == "get":
            # Todo: preguntar si tiene path, query o ambos
            return ResponseBuilder.request_successfull(request.queryString)
