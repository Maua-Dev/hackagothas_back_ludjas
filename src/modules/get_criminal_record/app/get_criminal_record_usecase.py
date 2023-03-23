from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetCriminalRecordsUsecase:
    def __init__(self, repo: ICriminalRecordRepository):
        self.repo = repo
        
    def __call__(self, criminal_record_id: int):
        if type(criminal_record_id) != int:
            raise EntityError('criminal_record_id')
        if criminal_record_id < 0:
            raise EntityError('criminal_record_id')

        criminal_record = self.repo.get_criminal_record(criminal_record_id)
        
        if criminal_record == None:
            raise NoItemsFound('criminal_record_id')
        
        return criminal_record