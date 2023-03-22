import pytest

from src.modules.get_criminal_records.app.get_criminal_records_controller import GetCriminalRecordsController
from src.modules.get_criminal_records.app.get_criminal_records_usecase import GetCriminalRecordsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordsController:
    
    def test_get_criminal_records_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        request = HttpRequest(query_params={'criminal_record_id': repo.criminal_records[0].criminal_record_id})
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'CriminalRecord was retrieved'
        assert response.body['CriminalRecord']['criminal_record_id'] == repo.criminal_records[0].criminal_record_id
        assert response.body['CriminalRecord']['criminal']['name'] == repo.criminal_records[0].criminal.name

    def test_get_criminal_records_controller_wrong_type_parameter(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        request = HttpRequest(query_params={'criminal_record_id': 'wrong_type'})
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field criminal_record_id isn't in the right type.\n Received: str.\n Expected: int"
        
    def test_get_criminal_records_controller_missing_parameter(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        request = HttpRequest(query_params={})
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field criminal_record_id is missing'
        
    def test_get_criminal_records_controller_no_items_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        request = HttpRequest(query_params={'criminal_record_id': 999})
        
        response = controller(request)
        
        assert response.status_code == 404
        assert response.body == 'No items found for criminal_record_id'
        
    def test_get_criminal_records_controller_entity_error(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        controller = GetCriminalRecordsController(usecase)
        
        request = HttpRequest(query_params={'criminal_record_id': -1})
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field criminal_record_id is not valid'