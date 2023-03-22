import pytest

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class TestCrime:
    def test_crime(self):
        crime = Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
        )
        
        assert crime.crime_id == 1
        assert crime.criminal.name == 'The Joker'
        assert crime.criminal.description == 'Dangerous criminal, usually seen with a smile on his face.'
        assert crime.criminal.gender == GENDER.MALE
        assert crime.criminal.region == 'Gotham'
        assert crime.criminal.height == 180
        assert crime.criminal.weight == 80
        assert crime.crime_type == CRIME_TYPE.HOMICIDE
        assert crime.description == 'Murdered 3 people in Gotham\'s streets.'
        assert crime.sentence == 10.0
    
    def test_crime_crime_id_not_int(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id="1",
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
            )
            
    def test_crime_crime_id_negative(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=-1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
            )
            
    def test_crime_criminal_not_criminal(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal='The Joker',
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
            )
            
    def test_crime_crime_type_not_crime_type(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type='HOMICIDE',
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
            )
            
    def test_crime_crime_type_not_in_enum(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=10.0
            )
            
    def test_crime_description_not_str(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description=[True],
            sentence=10.0
            )
            
    def test_crime_sentence_not_float(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence="10 anos em cárcere privado"
            )
            
    def test_crime_sentence_negative(self):
        with pytest.raises(EntityError):
            Crime(
            crime_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crime_type=CRIME_TYPE.HOMICIDE,
            description='Murdered 3 people in Gotham\'s streets.',
            sentence=-10.0
            )