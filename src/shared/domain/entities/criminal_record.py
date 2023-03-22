import abc
from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE

from src.shared.helpers.errors.domain_errors import EntityError

class CriminalRecord(abc.ABC):
    criminal_record_id: int
    criminal: Criminal
    crimes: List[CRIME_TYPE]
    is_arrested: bool

    def __init__(self, criminal_record_id: int, criminal: Criminal, crimes: List[CRIME_TYPE], is_arrested: bool):
        if type(criminal_record_id) != int:
            raise EntityError('criminal_record_id')
        if criminal_record_id < 0:
            raise EntityError('criminal_record_id')
        self.criminal_record_id = criminal_record_id

        if type(criminal) != Criminal:
            raise EntityError('criminal')
        self.criminal = criminal

        if type(crimes) != list:
            raise EntityError('crimes')
        if len(crimes) == 0:
            raise EntityError('crimes')
        for crime in crimes:
            if type(crime) != CRIME_TYPE:
                raise EntityError('crimes')
            if crime.value not in [crime.value for crime in CRIME_TYPE]:
                raise EntityError('crimes')
        self.crimes = crimes

        if type(is_arrested) != bool:
            raise EntityError('is_arrested')
        self.is_arrested = is_arrested