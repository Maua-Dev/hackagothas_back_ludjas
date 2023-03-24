from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_criminal_record_controller import GetCriminalRecordController
from .get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def lambda_handler(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = GetCriminalRecordUsecase(repo)
    controller = GetCriminalRecordController(usecase)
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()