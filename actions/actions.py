# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from domain_db.models import Gemuese
from sqlalchemy_tools.get_sqlalchemy_session import get_sqlalchemy_session

class ActionSearchGemuese(Action):
    
    def name(self) -> Text:
        return "action_search_gemuese"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        session = get_sqlalchemy_session()
        gemuese = tracker.get_slot(key="gemuese")
        message = "Die folgende {} sind angeboten:\n".format(gemuese)
        print("############## GEMUESE", gemuese)

        results = session.query(Gemuese).filter(Gemuese.typ==gemuese).all()
        print(results)
        for result in results:
            message += "{}\n".format(result)
        
        dispatcher.utter_message(text=message)

        return []
