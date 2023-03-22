from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CriminalRecordRepositoryMock:
    
    def test_get_criminal_records(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_records(criminal_record_id=1)
        
        assert type(criminal_record) == CriminalRecord
        assert criminal_record == repo.criminal_records[0]
        
    def test_get_criminal_records_not_found(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_records(criminal_record_id=999)
        
        assert criminal_record == None