from typing import List
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER

class CriminalViewmodel:
    name: str
    description: str
    gender: GENDER
    height: int
    weight: int

    def __init__(self, criminal: Criminal):
        self.name = criminal.name
        self.description = criminal.description
        self.gender = criminal.gender
        self.height = criminal.height
        self.weight = criminal.weight
        
    def to_dict(self) -> dict:
        return {
            "name" : self.name,
            "description" : self.description,
            "gender" : self.gender.value,
            "height" : self.height,
            "weight" : self.weight
        }

class GetCriminalRecordsViewmodel:
    criminal_record_id: int
    criminal: Criminal
    crimes = List[CRIME_TYPE]
    is_arrrested: bool
    
    def __init__(self, criminalRecord: CriminalRecord):
        self.criminal_record_id = criminalRecord.criminal_record_id
        self.criminal = criminalRecord.criminal
        self.crimes = criminalRecord.crimes
        self.is_arrested = criminalRecord.is_arrested
        
    def to_dict(self) -> dict:
        return {
            "CriminalRecord" : {
                "criminal_record_id" : self.criminal_record_id,
                "criminal" : CriminalViewmodel(self.criminal).to_dict(),
                "crimes" : [crime.value for crime in self.crimes],
                "is_arrested" : self.is_arrested
            },
            "message" : "CriminalRecord was retrieved"
        }