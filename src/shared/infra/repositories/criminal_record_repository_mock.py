from typing import List
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from typing import List


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    criminals: List[Criminal]
    crimes: List[Crime]
    criminal_records: List[CriminalRecord]

    def __init__(self):
        self.criminals = [
            Criminal(
                name="The Joker",
                description="The Joker is a supervillain and the archenemy of Batman. He was first introduced in Batman #1 (Spring 1940) and has remained consistently popular. The Joker is a master criminal with a clown-like appearance, and is considered one of the most infamous criminals within Gotham City.",
                gender=GENDER.MALE,
                height=175,
                weight=75,
                region='Gotham'
            ),
            Criminal(
                name="Harley Quinn",
                description="Harley Quinn is a supervillain and a frequent accomplice and lover of the Joker. She was first introduced in Batman: The Animated Series in 1992 and has since become a popular character in the Batman franchise. Harley Quinn is a former psychiatrist who became the Joker's assistant and later his partner in crime.",
                gender=GENDER.FEMALE,
                height=170,
                weight=63,
                region='Arkham'
            ),
            Criminal(
                name="The Penguin",
                description="The Penguin is a supervillain and one of Batman's oldest and most persistent enemies. He was first introduced in Detective Comics #58 (December 1941) and has since become a recurring villain in the Batman franchise. The Penguin is a short, portly man with a long nose and a fondness for birds and umbrellas. He is a master criminal who runs a variety of illegal enterprises in Gotham City.",
                gender=GENDER.MALE,
                height=165,
                weight=80,
                region='Gotham'
            ),
            Criminal(
                name="Catwoman",
                description="Catwoman is a supervillain and occasional ally of Batman. She was first introduced in Batman #1 (Spring 1940) as a jewel thief with a cat-like costume and a whip. Catwoman is a skilled fighter and acrobat, and is known for her complicated relationship with Batman.",
                gender=GENDER.FEMALE,
                height=168,
                weight=58,
                region='Gotham'
            ),
            Criminal(
                name="The Riddler",
                description="The Riddler is a supervillain and one of Batman's oldest enemies. He was first introduced in Detective Comics #140 (October 1948) and has since become a recurring villain in the Batman franchise. The Riddler is a criminal mastermind who leaves clues and puzzles for Batman to solve. He is known for his love of word games and riddles.",
                gender=GENDER.MALE,
                height=180,
                weight=70,
                region='Old Gotham'
            ),
            Criminal(
                name="Two-Face",
                description="Two-Face is a supervillain and one of Batman's most dangerous enemies. He was first introduced in Detective Comics #66 (August 1942) and has since become a recurring villain in the Batman franchise. Two-Face is a former district attorney who was disfigured by acid, causing him to develop a split personality. He is known for making decisions based on the flip of a coin.",
                gender=GENDER.MALE,
                height=183,
                weight=85,
                region='Penitentiary'
            ),
            Criminal(
                name="Scarecrow",
                description="Scarecrow is a supervillain and one of Batman's most fearsome enemies. He was first introduced in World's Finest Comics #3 (Fall 1941) and has since become a recurring villain in the Batman franchise. Scarecrow is a former professor of psychology who uses his knowledge of fear to terrorize the citizens of Gotham City.",
                gender=GENDER.MALE,
                height=183,
                weight=63,
                region='Chinatown'
            ),
            Criminal(
                name="Bane",
                description="Bane is a supervillain and one of Batman's most physically powerful enemies. He was first introduced in Batman: Vengeance of Bane #1 (January 1993) and has since become a recurring villain in the Batman franchise. Bane is a highly intelligent criminal who uses a drug called Venom to enhance his strength and endurance.",
                gender=GENDER.MALE,
                height=198,
                weight=120,
                region='Caribe'
            ),
            Criminal(
                name="Poison Ivy",
                description="Poison Ivy is a supervillain and eco-terrorist who uses her knowledge of plant biology to commit crimes. She was first introduced in Batman #181 (June 1966) and has since become a recurring villain in the Batman franchise. Poison Ivy has the ability to control plants and uses them to her advantage in her criminal schemes.",
                gender=GENDER.FEMALE,
                height=170,
                weight=57,
                region='Arkham'
            ),
        ]
        self.crimes = [
            Crime(
                crime_id=1,
                criminal=self.criminals[0],  # The Joker
                crime_type=CRIME_TYPE.BURGLARY,
                description="The joker robbed a store on 01/28/2023, taking three valuable jewels and holding three customers hostage. The crime was described as a challenge to Batman.",
                sentence=20
            ),
            Crime(
                crime_id=2,
                criminal=self.criminals[7],  # Bane
                crime_type=CRIME_TYPE.KIDNAPPING,
                description="Bane kidnapped the Mayor of Gotham City on 02/15/2023 and demanded a ransom of $5 million for his safe return. He was eventually apprehended by Batman and the Mayor was rescued.",
                sentence=25
            ),
            Crime(
                crime_id=3,
                criminal=self.criminals[8],  # Poison Ivy
                crime_type=CRIME_TYPE.TERRORISM,
                description="Poison Ivy carried out a series of attacks on corporations in Gotham City that she deemed responsible for environmental destruction. She used her ability to control plants to cause destruction and chaos, and was eventually stopped by Batman.",
                sentence=23
            ),
            Crime(
                crime_id=4,
                criminal=self.criminals[3],
                crime_type=CRIME_TYPE.ROBBERY,
                description="Catwoman stole a rare and valuable diamond necklace from a high-security museum in Gotham City on 03/18/2023. She used her agility and acrobatic skills to evade security measures and escape with the necklace.",
                sentence=5
            ),
        ]
        self.criminal_records = [
            CriminalRecord(
                criminal_record_id=1,
                criminal=self.criminals[0],
                crimes=[CRIME_TYPE.BURGLARY,
                        CRIME_TYPE.TERRORISM, CRIME_TYPE.HOMICIDE],
                is_arrested=False
            ),
            CriminalRecord(
                criminal_record_id=2,
                criminal=self.criminals[8],
                crimes=[CRIME_TYPE.KIDNAPPING,
                        CRIME_TYPE.THEFT, CRIME_TYPE.TERRORISM],
                is_arrested=False
            ),
            CriminalRecord(
                criminal_record_id=3,
                criminal=self.criminals[7],
                crimes=[CRIME_TYPE.ROBBERY,
                        CRIME_TYPE.ASSAULT, CRIME_TYPE.BATTERY],
                is_arrested=False
            ),
        ]

    def get_criminal_record(self, criminal_record_id: int) -> CriminalRecord:
        for record in self.criminal_records:
            if record.criminal_record_id == criminal_record_id:
                return record
        return None

    def delete_criminal_record(self, criminal_record_id: int) -> CriminalRecord:
        for idx in range(len(self.criminal_records)):
            if self.criminal_records[idx].criminal_record_id == criminal_record_id:
                criminal_record = self.criminal_records.pop(idx)
                return criminal_record
        return None
