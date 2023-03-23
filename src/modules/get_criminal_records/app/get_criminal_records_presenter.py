from .get_criminal_records_controller import GetCriminalRecordsController
from .get_criminal_records_usecase import GetCriminalRecordsUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def get_criminal_records_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = GetCriminalRecordsUsecase(repo)
    controller = GetCriminalRecordsController(usecase)
    
    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()