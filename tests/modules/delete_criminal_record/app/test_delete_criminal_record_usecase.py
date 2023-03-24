import pytest
from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock

class Test_DeleteCriminalRecordUsecase:
    
    def test_delete_criminal_record_usecase(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        crim_bef = repo.get_criminal_record(criminal_record_id=1)
        criminal_record = usecase(criminal_record_id=1)
        
        assert type(criminal_record) == CriminalRecord
        assert criminal_record == crim_bef
        
    def test_delete_criminal_record_usecase_no_items_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        
        with pytest.raises(NoItemsFound):
            criminal_record = usecase(criminal_record_id=999)
            
    def test_delete_criminal_record_usecase_entity_error(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        
        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id='a')