from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_criminal_record_controller import GetCriminalRecordController
from .get_criminal_record_usecase import GetCriminalRecordUsecase

repo = Environments.get_criminal_record_repo()()
usecase = GetCriminalRecordUsecase(repo=repo)
controller = GetCriminalRecordController(usecase=usecase)
def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()