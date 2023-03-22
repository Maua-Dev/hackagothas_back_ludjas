import pytest

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError

class TestCriminal:
    def test_criminal(self):
        criminal = Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region='Gotham',
            height=180,
            weight=80
        )
        
        assert criminal.name == 'The Joker'
        assert criminal.description == 'Dangerous criminal, usually seen with a smile on his face.'
        assert criminal.gender == GENDER.MALE
        assert criminal.region == 'Gotham'
        assert criminal.height == 180
        assert criminal.weight == 80
        
    def test_criminal_name_not_str(self):
        with pytest.raises(EntityError):
            Criminal(
                name=123,
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
            )

    def test_criminal_name_too_short(self):
        with pytest.raises(EntityError):
            Criminal(
                name="Jo",
                description='Dangerous criminal, usually seen with a smile on his face.',
                gender=GENDER.MALE,
                region='Gotham',
                height=180,
                weight=80
            )
            
    def test_criminal_description_not_str(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description=123,
            gender=GENDER.MALE,
            region='Gotham',
            height=180,
            weight=80
        )
    
    def test_criminal_description_too_short(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous',
            gender=GENDER.MALE,
            region='Gotham',
            height=180,
            weight=80
        )
            
    def test_criminal_gender_not_gender(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender="MALE",
            region='Gotham',
            height=180,
            weight=80
        )
            
    def test_criminal_gender_not_in_GENDER(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER,
            region='Gotham',
            height=180,
            weight=80
        )
            
    def test_criminal_region_not_str(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region=123,
            height=180,
            weight=80
        )
            
    def test_criminal_height_not_int(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region='Gotham',
            height="Um metro e oitenta centímetros",
            weight=80
        )
    
    def test_criminal_height_negative(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region='Gotham',
            height=-18,
            weight=80
        )
            
    def test_criminal_weight_not_int(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region='Gotham',
            height=180,
            weight="Oitenta quilos"
        )
            
    def test_criminal_weight_negative(self):
        with pytest.raises(EntityError):
            Criminal(
            name='The Joker',
            description='Dangerous criminal, usually seen with a smile on his face.',
            gender=GENDER.MALE,
            region='Gotham',
            height=180,
            weight=-8
        )