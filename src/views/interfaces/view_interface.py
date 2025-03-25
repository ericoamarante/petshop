from abc import ABC, abstractmethod
from src.views.http_types.http_requet import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
