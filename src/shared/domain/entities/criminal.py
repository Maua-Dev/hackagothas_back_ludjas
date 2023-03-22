import abc

from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class Criminal(abc.ABC):
    name: str
    description: str
    gender: GENDER
    region: str
    height: int # cm
    weight: int # kg
    NAME_MIN_LENGTH = 3
    DESC_MIN_LENGTH = 10

    def __init__(self, name: str, description: str, gender: GENDER, region: str, height: int, weight: int):
        if type(name) != str:
            raise EntityError('name')
        if len(name) < self.NAME_MIN_LENGTH:
            raise EntityError('name')
        self.name = name
        
        if type(description) != str:
            raise EntityError('description')
        if len(description) < self.DESC_MIN_LENGTH:
            raise EntityError('description')
        self.description = description
        
        if type(gender) != GENDER:
            raise EntityError('gender')
        if gender.value not in [gender.value for gender in GENDER]:
            raise EntityError('gender')
        self.gender = gender
        
        if type(region) != str:
            raise EntityError('region')
        self.region = region

        if type(height) != int:
            raise EntityError('height')
        if height < 0:
            raise EntityError('height')
        self.height = height

        if type(weight) != int:
            raise EntityError('weight')
        if weight < 0:
            raise EntityError('weight')
        self.weight = weight

