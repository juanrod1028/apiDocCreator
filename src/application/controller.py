from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.useCase.service.service import Service
from src.useCase.models.request import Request


app = FastAPI()
service = Service()


@app.post("/hi")
def read_item(request: Request) -> JSONResponse:

    return service.create_apidoc(request)
