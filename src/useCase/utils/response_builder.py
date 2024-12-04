from typing import final
from fastapi import status
from fastapi.responses import JSONResponse
from src.useCase.models.response import Response
from src.useCase.constants.constants import Constants


class ResponseBuilder:
    @staticmethod
    @final
    def request_successfull(parameter: dict | str) -> JSONResponse:
        response = Response(
            status=status.HTTP_200_OK,
            message=Constants.SUCCES_MESSAGE,
            apiDoc=parameter,
        )
        return JSONResponse(content=response.dict(),
                            status_code=status.HTTP_200_OK,
                            headers={"X-Custom-Header": "Request Successful"})
