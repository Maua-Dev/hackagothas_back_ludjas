from src.modules.get_criminal_records.app.get_criminal_records_viewmodel import GetCriminalRecordsViewmodel
from src.modules.get_criminal_records.app.get_criminal_records_usecase import GetCriminalRecordsUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class GetCriminalRecordsController:
    
    def __init__(self, usecase: GetCriminalRecordsUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('criminal_record_id') is None:
                raise MissingParameters('criminal_record_id')
            
            if type(request.data.get('criminal_record_id')) is not int:
                raise WrongTypeParameter(
                    fieldName='criminal_record_id',
                    fieldTypeExpected='int',
                    fieldTypeReceived=request.data.get('criminal_record_id').__class__.__name__
                )            
                
            criminal_record = self.usecase(criminal_record_id=request.data.get('criminal_record_id'))
            
            viewmodel = GetCriminalRecordsViewmodel(criminalRecord=criminal_record)
            
            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])