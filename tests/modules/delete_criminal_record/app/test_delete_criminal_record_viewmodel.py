from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordsViewmodel:
    
    def test_get_criminal_record_viewmodel(self):
        repo = CriminalRecordRepositoryMock()
        
        criminal_record = repo.delete_criminal_record(criminal_record_id=1)
        viewmodel = DeleteCriminalRecordViewmodel(criminal_record).to_dict()
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
                    'message':'CriminalRecord was deleted'
                    }
        assert viewmodel == expected