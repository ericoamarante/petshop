from src.controllers.person_finder_controller import PersonFinderController
from .interfaces.view_interface import ViewInterface
from .http_types.http_requet import HttpRequest
from .http_types.http_response import HttpResponse

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        body_response = self.__controller.find(person_id)

        return HttpResponse(status_code=201, body=body_response)
