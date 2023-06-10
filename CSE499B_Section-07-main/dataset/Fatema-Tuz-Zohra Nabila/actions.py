# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action


class ActionHelloWorld(Action):

     def name(self) -> Text:
        return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []



class ActionHospitalWiseHeartDoctorSearch(Action):

    def name(self) -> Text:
        return "action_heart_wise_hospital_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'heart':
                name = e['value']

            if name == "AMZ Hospital":
                message = "Here are some of the cardiac specialist in AMZ Hospital. You can check out from here- Prof. Dr. Col. Md. Abdul Hannan , Dr. Harun-ur-Rashid Bhuiyan ,  Dr. Abu Hasnat Md. Masud Sinha"
  
            if name == "Al-Manar Hospital":
                message = "Here are some of the cardiac specialist in Al-Manar Hospital. You can check out from here- Dr. Mohammad Zakir Hossain, Prof. Dr. Nurul Alam Talukder"

            if name == "City Hospital":
                message = "Here are some of the cardiac specialist in City Hospital & Diagnostic Center. You can check out from here- Prof. Dr. KMHS Sirajul Haque , Dr. Azizul Bari, Dr. Md. Arif Hossain"
           
            if name == "Dhaka Central Medical College":
                message = "Currently there are no Cardiac Specialist in Dhaka Central International Medical College"

            if name == "Bangladesh Specialized Hospital":
                message = "Here are some of the cardiac specialist in Bangladesh Specialized Hospital. You can check out from here-Dr. Khalifa Mahmud Tarik, Dr Md. Shaukat Ali"
            
            if name == "Labaid Hospital":
                message = "Here are some of the cardiac specialists in Labaid Hospital. You can check out from here- Dr. Md. Lokman Hossain, Dr. Amirul Islam Bhuyan, Dr. Nurun Nahar Fatema Begum, Dr. Akhter Hamid Parvez , Dr. Arun Kumar Sharma"

            if name == "Square Hospital":
                message = "Here are some of the cardiac specialists in Square Hospital. You can check out from here- Dr. Kamal Pasha, Dr. SM Shahedul Amin Robin, Dr. Asif Manwar"

            if name == "Ibn Sina":
                message = "Here are some of the cardiac specialists in Ibn Sina Hospital. You can check out from here- Dr. Nirmal Kanti Dey, Dr. Md. Zakir Hossain, Dr. Rakibul Hasan Apu"

            if name == "Medinova Hospital":
                message = "Currently there are no Cardiologist in Medinova Hospital."

            if name == "United Hospital":
                message = "Here are some of the cardiac specialists in United Hospital. You can check out from here- Dr. Fatema Begum, Dr. Rezaul Hassan, Dr. A. M. Shafique"




        dispatcher.utter_message(text=message)

        return []

class ActionHospitalWiseCancerDoctorSearch(Action):

    def name(self) -> Text:
        return "action_cancer_wise_hospital_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'cancer':
                name = e['value']

  
            if name == "Al-Manar Hospital":
                message = "Currently there are no oncologists in Al-Manar Hospital."

            if name == "City Hospital":
                message = "Here are some of the cancer specialist in City Hospital & Diagnostic Center. You can check out from here- Prof. Dr. Md. Ehteshamul Hoque"
           
            if name == "Dhaka Central Medical College":
                message = "Here are some of the cancer specialist in Dhaka Central Medical College. You can check out from here- Dr. M Safiul Alam"

            if name == "Bangladesh Specialized Hospital":
                message = "Here are some of the cancer specialist in Bangladesh Specialized Hospital. You can check out from here- Prof. Dr. Qamruzzaman Chowdhury, Dr. Ferdous Ara Begum, Dr. Md. Arifur Rahman"
            
            if name == "Labaid Hospital":
                message = "Here are some of the cancer specialist in Labaid Hospital. You can check out from here- Dr. A.F.M. Kamal Uddin, Prof. Dr. Qazi Mushtaq Hussain"

            if name == "Square Hospital":
                message = "Here are some of the cancer specialists in Square Hospital. You can check out from here- Dr. Arunangshu Das, Dr. Md. Salim Reza, Prof. Syed Md. Akram Hussain"

            if name == "Ibn Sina":
                message = "Here are some of the cancer specialists in Ibn Sina Hospital. You can check out from here- Prof. Dr. Zafor Md. Masum"

            if name == "Medinova Hospital":
                message = "Currently there are no Oncologist in Medinova Hospital"

            if name == "United Hospital":
                message = "Here are some of the cancer specialists in United Hospital. You can check out from here- Dr. Rashid Un Nabi, Dr. Ashim Kumar Sengupta"


        dispatcher.utter_message(text=message)

        return []


class ActionHospitalWiseChildDoctorSearch(Action):

    def name(self) -> Text:
        return "action_child_wise_hospital_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'child':
                name = e['value']

            if name == "Al-Manar Hospital":
                message = "Here are some of the child specialists in Al-Manar Hospital. You can check out from here- PROF. Dr. M.A.K. AZAD CHOWDHURY, Prof. Chowdhury Md. Haider Ali, Dr. Sultan Ahmed, Dr. Mohammad Abdul Hai, Dr. Kazi Md. Noor-Ul Ferdous"

            if name == "City Hospital":
                message = "Currently there are no paediatrician in City Hospital"
           
            if name == "Dhaka Central Medical College":
                message = "Here are some of the child specialist in Dhaka Central Medical College. You can check out from here- Dr. Mahbubul Alam"

            if name == "Bangladesh Specialized Hospital":
                message = "Here are some of the child specialist in Bangladesh Specialized Hospital. You can check out from here- Dr. Ahmed Zahid Hossain, Prof. Dr. Abdul Hanif (Tablu)"
            
            if name == "Labaid Hospital":
                message = "Here are some of the child specialist in Labaid Hospital. You can check out from here- Dr. Amina Akter, Dr. Musrat Rahman Deeba, Dr. Mahmuda Zaman"

            if name == "Square Hospital":
                message = "Here are some of the child specialist in Square Hospital. You can check out from here- Prof. Dr. ABM Abdus Salam, Dr. Lutfun Nahar Begum"

            if name == "Ibn Sina":
                message = "Here are some of the child specialist in Ibn Sina Hospital. You can check out from here- Dr. Rumana Choudhury, Dr. Tahmina Karim , Dr. Shahin Akter"

            if name == "Medinova Hospital":
                message = "Here are some of the child specialist in Medinova Hospital. You can check out from here- Prof. Dr. Nazma Begum"

            if name == "United Hospital":
                message = "Here are some of the child specialist in United Hospital. You can check out from here- Dr. Kaniz Hasina, Dr. Prof. Md. Salim Shakur PhD"




        dispatcher.utter_message(text=message)

        return []


