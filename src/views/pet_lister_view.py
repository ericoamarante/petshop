from src.controllers.pet_lister_controller import PetListerController
from .interfaces.view_interface import ViewInterface
from .http_types.http_requet import HttpRequest
from .http_types.http_response import HttpResponse

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)
