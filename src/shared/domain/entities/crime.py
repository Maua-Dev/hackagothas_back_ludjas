import abc

from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.entities.criminal import Criminal
from src.shared.helpers.errors.domain_errors import EntityError


class Crime(abc.ABC):
    crime_id: int
    criminal: Criminal
    crime_type: CRIME_TYPE
    description: str
    sentence: float # years
    description_min_length = 10

    def __init__(self, crime_id: int, criminal: Criminal, crime_type: CRIME_TYPE, description: str, sentence: float):
        if type(crime_id) != int:
            raise EntityError('crime_id')
        if crime_id < 0:
            raise EntityError('crime_id')
        self.crime_id = crime_id

        if type(criminal) != Criminal:
            raise EntityError('criminal')
        self.criminal = criminal

        if type(crime_type) != CRIME_TYPE:
            raise EntityError('crime_type')
        if crime_type.value not in [crime_type.value for crime_type in CRIME_TYPE]:
            raise EntityError('crime_type')
        self.crime_type = crime_type

        if type(description) != str:
            raise EntityError('description')
        if len(description) < self.description_min_length:
            raise EntityError('description')
        self.description = description
        
        if type(sentence) == int:
            sentence = float(sentence)
        if type(sentence) != float:
            raise EntityError('sentence')
        if sentence < 0:
            raise EntityError('sentence')
        self.sentence = sentence
        