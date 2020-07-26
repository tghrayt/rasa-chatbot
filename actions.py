# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any
from typing import Text
from typing import Dict
from typing import List

from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import requests
 
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

        def name(self) -> Text:
            return "action_hello_cih"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(text="Hello , this is cih bank ")

            return []

class ActionNumClass(Action):
    
        def name(self) -> Text:
            return "action_num_class"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

             response = requests.get("http://localhost:8081/listStudent").json()
             print(response)

             entities= tracker.latest_message.get('text')
             print("Last message now"+ entities)

             state=None
             resData=""
             state = entities
             for data in response:
                 if data["firstName"]==state:
                     print(data)
                     resData="firstName: "+data["firstName"]+" || lastName: "+data["lastName"]+" || type de compte :"+data["compte"]+" || avec un solde de  :"+data["solde"]+"Dhs"     
                     

            
             dispatcher.utter_message(text=resData)

             return []            