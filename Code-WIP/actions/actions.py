# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
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

import requests
import json

# API to access COVID related information
cases_by_dist = requests.get(
    'https://data.covid19india.org/v4/min/data.min.json')


# state vs state code mapping

statecode_to_state = {"state_mappings":
                      {'tt': 'Total', 'kl': 'Kerala', 'dl': 'Delhi', 'tg': 'Telangana', 'rj': 'Rajasthan', 'hr': 'Haryana', 'up': 'Uttar Pradesh', 'la': 'Ladakh', 'tn': 'Tamil Nadu', 'jk': 'Jammu and Kashmir', 'ka': 'Karnataka', 'mh': 'Maharashtra', 'pb': 'Punjab', 'ap': 'Andhra Pradesh', 'ut': 'Uttarakhand', 'or': 'Odisha',
                       'py': 'Puducherry', 'wb': 'West Bengal', 'ch': 'Chandigarh', 'ct': 'Chhattisgarh', 'gj': 'Gujarat', 'hp': 'Himachal Pradesh', 'mp': 'Madhya Pradesh', 'br': 'Bihar', 'mn': 'Manipur', 'mz': 'Mizoram', 'ga': 'Goa', 'an': 'Andaman and Nicobar Islands', 'jh': 'Jharkhand', 'as': 'Assam', 'ar': 'Arunachal Pradesh', 'tr': 'Tripura', 'ml': 'Meghalaya'}}
state_to_statecode = {"state_mappings":
                      {'Total': 'tt', 'Kerala': 'kl', 'Delhi': 'dl', 'Telangana': 'tg', 'Rajasthan': 'rj', 'Haryana': 'hr', 'Uttar Pradesh': 'up', 'Ladakh': 'la', 'Tamilnadu': 'tn', 'Jammu and Kashmir': 'jk', 'Karnataka': 'ka', 'Maharashtra': 'mh', 'Punjab': 'pb', 'Andhra Pradesh': 'ap', 'Uttarakhand': 'ut', 'Odisha': 'or', 'Puducherry': 'py', 'West Bengal': 'wb', 'Chandigarh': 'ch', 'Chhattisgarh': 'ct', 'Gujarat': 'gj', 'Himachal Pradesh': 'hp', 'Madhya Pradesh': 'mp', 'Bihar': 'br', 'Manipur': 'mn', 'Mizoram': 'mz', 'Goa': 'ga', 'Andaman and Nicobar Islands': 'an', 'Jharkhand': 'jh', 'Assam': 'as', 'Arunachal Pradesh': 'ar', 'Tripura': 'tr', 'Meghalaya': 'ml'}}


def get_dist_based_state(state):
    case_dict = {}
    for s in cases_by_dist.json().keys():
        if(s == state):
            for place, val in zip(cases_by_dist.json()[state]['total'].keys(), cases_by_dist.json()[state]['total'].values()):
                case_dict[place] = val
    return case_dict


class ActionTellCases(Action):

    def name(self) -> Text:
        return "action_tell_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cur_state = next(tracker.get_latest_entity_values("state"), None)
        if(cur_state != None):
            state = (state_to_statecode['state_mappings'][cur_state]).upper()
            cases = get_dist_based_state(state)
            dispatcher.utter_message("Here is the statistics for {}: \n Active Cases: {} Confirmed Cases: {} Deceased: {} Recovered: {} ".format(
                cur_state, cases['confirmed']-cases['deceased']-cases['recovered'], cases['confirmed'], cases['deceased'], cases['recovered']))
        else:
            dispatcher.utter_message("Enter with Location ")
        return []
