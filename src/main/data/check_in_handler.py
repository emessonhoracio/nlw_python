from src.models.repository.check_ins_repository import CheckInsRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_repository = CheckInsRepository() 

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        check_in_infos = http_request.param["attendee_id"]
        # print(check_in_infos)
        http_response = self.__check_in_repository.insert_check_in(check_in_infos)

        return HttpResponse(
            body=None,
            status_code=201
        )