from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CriminalRecordRepositoryMock:
    
    def test_get_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_record(criminal_record_id=1)
        
        assert type(criminal_record) == CriminalRecord
        assert criminal_record == repo.criminal_records[0]
        
    def test_get_criminal_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_record(criminal_record_id=999)
        
        assert criminal_record == None
        
    def test_delete_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        len_before = len(repo.criminal_records)
        criminal_record = repo.delete_criminal_record(criminal_record_id=1)
        assert len(repo.criminal_records) == len_before - 1
        assert criminal_record != repo.criminal_records[0]