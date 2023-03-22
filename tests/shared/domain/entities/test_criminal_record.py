import pytest
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class TestCriminalRecord:
    def test_criminal_record(self):
        criminal_record = CriminalRecord(
            criminal_record_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=[CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY],
            is_arrested=False
            )

        assert criminal_record.criminal_record_id == 1
        assert criminal_record.criminal.name == 'The Joker'
        assert criminal_record.criminal.description == 'Dangerous criminal, usually seen with a smile on his face.'
        assert criminal_record.criminal.gender == GENDER.MALE
        assert criminal_record.criminal.region == 'Gotham'
        assert criminal_record.criminal.height == 180
        assert criminal_record.criminal.weight == 80
        assert criminal_record.crimes == [CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY]
        assert criminal_record.is_arrested == False
        
    def test_criminal_record_criminal_record_id_not_int(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id="1",
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=[CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY],
            is_arrested=False
            )
            
    def test_criminal_record_criminal_record_id_negative(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=-1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=[CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY],
            is_arrested=False
            )
            
    def test_criminal_criminal_not_criminal(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=1,
            criminal="The Joker",
            crimes=[CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY],
            is_arrested=False
            )
    
    def test_criminal_crimes_not_list(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=CRIME_TYPE.HOMICIDE,
            is_arrested=False
            )
        
    def test_criminal_crimes_empty(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=[],
            is_arrested=False
            )
    
    def test_criminal_crimes_not_crime_type(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=["HOMICIDE", "ROBBERY"],
            is_arrested=False
            )
            
    def test_criminal_is_arrested_not_bool(self):
        with pytest.raises(EntityError):
            CriminalRecord(
            criminal_record_id=1,
            criminal=Criminal(
                name='The Joker',
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
                ),
            crimes=[CRIME_TYPE.HOMICIDE, CRIME_TYPE.ROBBERY],
            is_arrested="No"
            )