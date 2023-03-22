from src.modules.get_criminal_records.app.get_criminal_records_viewmodel import GetCriminalRecordsViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordsViewmodel:
    
    def test_get_criminal_records_viewmodel(self):
        repo = CriminalRecordRepositoryMock()
        
        criminal_record = repo.criminal_records[0]
        viewmodel = GetCriminalRecordsViewmodel(criminal_record).to_dict()
        expected = {
                    'CriminalRecord':{
                        'criminal_record_id':1,
                        'criminal':{
                            'name':'The Joker',
                            'description':'The Joker is a supervillain and the archenemy of Batman. He was first introduced in Batman #1 (Spring 1940) and has remained consistently popular. The Joker is a master criminal with a clown-like appearance, and is considered one of the most infamous criminals within Gotham City.',
                            'gender':"MALE",
                            'height':175,
                            'weight':75
                        },
                        'crimes':["BURGLARY", "TERRORISM", "HOMICIDE"],
                        'is_arrested':False
                    },
                    'message':'CriminalRecord was retrieved'
                    }
        assert viewmodel == expected
        
        