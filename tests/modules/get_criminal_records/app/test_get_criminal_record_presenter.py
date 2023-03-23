import json
from src.modules.get_criminal_record.app.get_criminal_record_presenter import get_criminal_record_presenter

class Test_GetCriminalRecordsPresenter:
    def test_get_criminal_record_presenter(self):
        event = {
            "body": {
                "criminal_record_id": "1"
            }
        }
        response = get_criminal_record_presenter(event, None)
        
        expected = {
                'CriminalRecord':{
                    'criminal_record_id':1,
                    'criminal':{
                        'name':'The Joker',
                        'description':'The Joker is a supervillain and the archenemy of Batman. He was first introduced in Batman #1 (Spring 1940) and has remained consistently popular. The Joker is a master criminal with a clown-like appearance, and is considered one of the most infamous criminals within Gotham City.',
                        'gender':'MALE',
                        'height':175,
                        'weight':75
                    },
                    'crimes':[
                        'BURGLARY',
                        'TERRORISM',
                        'HOMICIDE'
                    ],
                    'is_arrested':False
                },
                'message':'CriminalRecord was retrieved'
                }
        
        assert response["status_code"] == 200
        assert json.loads(response['body']) == expected
        
    def test_get_criminal_record_presenter_no_items_found(self):
        event = {
            "body": {
                "criminal_record_id": "777"
            }
        }
        response = get_criminal_record_presenter(event, None)
        
        assert response['status_code'] == 404
        assert json.loads(response['body'])== "No items found for criminal_record_id"