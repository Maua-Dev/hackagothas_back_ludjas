import pytest
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordsUsecase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalUsecase:
    def test_get_criminal_record_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        criminal_record = usecase(criminal_record_id=1)
        
        assert type(criminal_record) == CriminalRecord
        assert criminal_record == repo.criminal_records[0]
    
    def test_get_criminal_record_usecase_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        
        with pytest.raises(NoItemsFound):
            usecase(criminal_record_id=777)
            
    def test_get_criminal_record_usecase_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordsUsecase(repo)
        
        with pytest.raises(EntityError):
            usecase(criminal_record_id=-1)