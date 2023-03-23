from abc import ABC, abstractmethod

from src.shared.domain.entities.criminal_record import CriminalRecord

class ICriminalRecordRepository(ABC):
    
    @abstractmethod
    def get_criminal_record(self, criminal_record_id: int) -> CriminalRecord:
        pass