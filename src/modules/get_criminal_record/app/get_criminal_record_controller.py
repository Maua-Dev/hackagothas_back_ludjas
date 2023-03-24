from src.modules.get_criminal_record.app.get_criminal_record_viewmodel import GetCriminalRecordViewmodel
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class GetCriminalRecordController:
    
    def __init__(self, usecase: GetCriminalRecordUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.query_params.get('criminal_record_id') is None:
                raise MissingParameters('criminal_record_id')
            
            if type(request.query_params.get('criminal_record_id')) is not str:
                raise WrongTypeParameter(
                    fieldName='criminal_record_id',
                    fieldTypeExpected='str',
                    fieldTypeReceived=request.data.get('criminal_record_id').__class__.__name__
                )            
                
            if not request.data.get('criminal_record_id').isdecimal():
                raise EntityError('criminal_record_id')
                
            criminal_record = self.usecase(criminal_record_id=int(request.data.get('criminal_record_id')))
            
            viewmodel = GetCriminalRecordViewmodel(criminalRecord=criminal_record)
            
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