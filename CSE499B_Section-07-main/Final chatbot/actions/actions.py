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


    ## Action heart wise hospital search

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




## Action cancer wise hospital search


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

    ## Action child wise hospital search

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



# Area wise hospital [Name]-

class Actionhospitalsearchbyarea(Action):

    def name(self) -> Text:
        return "action_hospital_search_by_area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'area':
                name = e['value']
            if name == "Mohammadpur":
                message = "Some Hospitals in Mohammadpur are- Al-Manar Hospital, City Hospital & Diagnostic Center, Dhaka Central International Medical College, Bangladesh Specialized Hospital"
            if name == "Mirpur":
                message = "Some Hospitals in Mirpur are- Mirpur general hospitals & diagnostic centre, Dr Azmal hospital                                                   , Mirpur holy crescent hospital, Al helal specialized hospital dhaka"
            if name == "Bashundhara":
                message = "Some Hospitals in Bashundhara are- AMZ hospital, Evercare hospital, Central hospital, Baridhara general hospital"
            if name == "Dhanmondi":
                message = "Some Hospitals in Dhanmondi are-Labaid Hospital Dhanmondi,Square Hospital, Dhaka,Ibn Sina Hospital Dhanmondi,Medinova Hospital, Dhanmondi"
            if name == "Gulshan":
                message = "Some Hospitals in Banani and Gulshan are- United Hospital Dhaka"

        dispatcher.utter_message(text=message)

        return []

# Disease wise hospital [Name]
class ActionHospitalSearchByDisease(Action):

    def name(self) -> Text:
        return "action_hospital_search_by_disease"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'problem_type_hospital':
                name = e['value']
            if name == "heart":
                message = "Here are some of the best heart specialized hospitals in Dhaka- National Heart Foundation Hospital, Cardiac Electrophysiology & Heart Failure Center, Ibrahim Cardiac Hospital & Research Institute,LABAID Cardiac Hospital ,Millennium Heart & General Hospital Ltd"
            if name == "cancer":
                message = "Here are some of the best cancer hospitals Ahsania Mission Cancer Hospital, National Institute of cancer Research & Hospital (NICRH) ,Ahsania Mission Cancer & General Hospital,Labaid Cancer Hospital And,The ENT and Head Cancer Hospital and Institute"
            if name == "child":
                message = "Here are some of the child hospitals - Dhaka Shishu (Children) Hospital,Dr. MR Khan Shishu hospital & Institute of Child Health, Dhaka Paediatric-Neonatal & General Hospital Limited"
   


        dispatcher.utter_message(text=message)

        return []


# Hospital Address [Name]
class ActionHospitalAddress(Action):

    def name(self) -> Text:
        return "action_Hospital_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'hospital_name':
                name = e['value']
            if name == "Al-Manar Hospital":
                message = "Here is the address of Al-Manar Hospital - Plot No: Umo, Block No: Rossoi, Satmosjid Road, Mohammadpur, Dhaka-1207, Tel: 02-9121387, 02-9121588, Mobile: 015500-20871,015500-20885, E-mail:almanarhospital1996@gmail.com"
            if name == "City Hospital & Diagnostic Center":
                message = "Here is the address: City Hospital & Diagnostic Center - Mailing Address: 1/8, Block-E, Lalmatia, Satmosjid Road, Mohammadpur, Dhaka - 1207. Telephone 8143312, 8143437, 8143166, 8143167, 9124436 Mobile (Hotline) +88 01558220134,  +88 01815 484600 Email, cityhosp.bd@gmail.com & info@cityhospitalbd.com "
            if name == "Dhaka Central  Medical College":
                message = "Here is the address: Dhaka Central  Medical College - 2/1 Ring Road, Shyamoli Dhaka - 1207, Bangladesh P: +88 02 48117801, +88 02 48118638, +88 02 48117802, +88 02 48118639,+88 02 48122739, +88 02 48122740, F: +88-02-9118598 M: +880 1755 597 798, +880 1755 630 167,E: director@dcimch.com"
            if name == "Bangladesh Specialized Hospital":
                message = "Here is the address: Bangladesh Specialized Hospital - 21 Shyamoli, Mirpur Road, Dhaka-1207, Bangladesh Phone: 10633, +8809666700100, Mail :info@bshl.com.bd ,bshl.dhaka@gmail.com "
            if name == "Labaid Hospital":
                message = "Here is the address: Labaid Hospital -Address: House # 6, Road # 4, Dhanmondi, Dhaka, Contact: 10606, +8801713333337"
            if name == "Square Hospital":
                message = "Here is the address: Square Hospital - Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact: 10616, +8801713141447"
            if name == "Ibn Sina Hospital":
                message = "Here is the address: Ibn Sina Hospital -Ibn Sina Specialized Hospital, Dhanmondi Address: House # 68, Road # 15/A, Dhanmondi, Dhaka,Contact: +8801823039800, +880255029101"
            if name == "Medinova Hospital":
                message = "Here is the address: Medinova Hospital - Address: House # 71/A, Road # 5/A, Dhanmondi R/A, Dhaka Contact: +8801796222222, +8801750557722 "
            if name == "United Hospital Dhaka":
                message = "Address:  United Hospital Dhaka: Plot # 15 Rd No 71, Dhaka 1212 Hours: Open 24 hour"
            if name == "AMZ hospital":
                message = "Address: AMZ hospital : Cha- 80/3, Shadhinota Sarani, Progati Sarani Rd, Dhaka 1212, Phone: 01847-331010, Email : info@amzhospitalbd.com"
            if name == "Evercare hospital":
                message = "Address: Evercare hospital 	: Plot: 81, Block: E, Bashundhara R/A, Dhaka 1229, Bangladesh. Hotline 	: 10678. Whatsapp 	: +880 1713-047455. E-mail 	: feedback@evercarebd.com. "
            if name == "Central hospital":
                message = "Address: Central hospital : House # 2, Road # 5, Green Road Dhanmondi, Dhaka, Bangladesh, Phone : +880 2 9660015-19, 8624514-9,  Fax : +880 2 8619321,  Email: chl@bol-online.com,   Web: http://www.centralhospitalltd.com "
            if name == "Baridhara general hospital":
                message = "Address: Baridhara general hospital : Ka-54/1 Progoti Sharani, Nadda, Gulshan, Dhaka-1212 , Phone: 01768612835, Email: bghospital.bd@gmail.com  "
            if name == "Mirpur general hospitals & diagnostic centre":
                message = "Address: Mirpur general hospitals & diagnostic centre:  House # 12/8-68, Road # 4, Block # B, Section # 12, Pallabi, Mirpur, Dhaka- 1216, Bangladesh, Phone: 01785-906599 "
            if name == "Dr Azmal hospital":
                message = "Address: Dr Azmal hospital : Plot NO#5, Road#4, Block#A,. Section#6, Mirpur,  Cell phone: +88 01914 48 83 45,  Telephone: +88 02 9005085/ 9013271/ 8033245/ 8051974 ,  Email:info@azmalhospital.com.  "
            if name == "Mirpur holy crescent hospital":
                message = "Address: Mirpur holy crescent hospital: 49 South Bishil, Road-10, Mirpur-1, Dhaka, Bangladesh, Phone: 01913-821665, Email : hchl500@yahoo.com "
            if name == "Al helal specialized hospital dhaka":
                message = "Adress: Al helal specialized hospital dhaka : 150, Begum Rokeya Sarani, Senpara-Parbata, Mirpur-10, Dhaka, Phone:  +88-02-9906820, 029032763,  +88-02-9906820, Email:  ahshcorp@gmail.com"
            if name == "National Heart Foundation Hospital":
                message = "Here is the Address: National Heart Foundation Hospital:  Plot # 7/2, Section # 2, Mirpur, Dhaka. Telephone +880258051355, +880258051365, Email - admin@nhf.org.bd, nhfadmin@agni.com , Mobile (Hotline)-  58054708-12 (X-101), Opening and closing time - Thursday - 8:30am to 9:00pm "
            if name == "Cardiac Electrophysiology & Heart Failure Center":
                message = "Here is the Address: Cardiac Electrophysiology & Heart Failure Center-  OPD L-5, Apollo Hospitals, Plot: 81, Block:E Dhaka Dhaka, 1229 ,Telephone- 09666-710678,"
            if name == "Ibrahim Cardiac Hospital & Research Institute":
                message = "Here is the Address: Ibrahim Cardiac Hospital & Research Institute- 122 Kazi Nazrul Islam Ave, Dhaka 1000, Telephone- (8802) 9671141, Mobile (Hotline)- (88) 01713 003004, Email- info@ibrahimcardiac.org.bd, Opening and closing time "
            if name == "LABAID Cardiac Hospital":
                message = "Here is the Address: LABAID Cardiac Hospital- House- 01 & 03, Road-04, Dhanmondi. Dhaka 1205, Bangladesh, Telephone- +88 02 9676356,+88 02 58610793-8, Mobile (Hotline)- 10606, Email- registrar.emergency@labaidgroup.com"
            if name == "Millennium Heart & General Hospital Ltd":
                message = "Here is the Address: Millennium Heart & General Hospital Ltd- 4/9 Block-F ,Lalmatia, Dhaka-1207. Telephone- 9122115 , 8120097 , 9124046, 01920151757 "
            if name == "Ahsania Mission Cancer Hospital":
                message = "Here is the Address: Ahsania Mission Cancer Hospital- House # 19, Road # 12 (New) , Dhanmondi R/A, Dhaka-1209, Bangladesh,Telephone- (880-2) 9127943, Mobile (Hotline)- 9123402,Email- dambgd@ahsaniamission.org.bd, "
            if name == "National Institute of cancer Research & Hospital":
                message = "Here is the Address: National Institute of cancer Research & Hospital- Mohakhali, TB Gate Road Dhaka-1212, Bangladesh, Telephone-  (+88222280078),Email- nicrh@hospi.dghs.gov.bd"
            if name == "Ahsania Mission Cancer & General Hospital":
                message = "Here is the Address: Ahsania Mission Cancer & General Hospital- Plot # 03, Embankment Drive Way, Sector-10, Uttara Model Town, Uttara, Dhaka-1230, Telephone- 09678016391,09612310617, Mobile (Hotline)- 10617, Email- amcgh.info@gmail.com"
            if name == "Labaid Cancer Hospital":
                message = "Here is the Address: Labaid Cancer Hospital- House-06, Road-04, Dhanmondi, Dhaka 1205. Telephone- 01766662111, Mobile (Hotline)- 10606, Email- info@labaidgroup.com"
            if name == "ENT and Head Cancer Hospital and Institute":
                message = "Here is the Address: ENT and Head Cancer Hospital and Institute- Plot No.-F- 12, Sher-e-Bangla Nagar ,Dhaka- 1207, Bangladesh, Telephone- +88 02 58151660, Email- zntcancerhospital@yahoo.com,"
            if name == "Dhaka Shishu (Children) Hospital":
                message = "Here is the Address: Dhaka Shishu (Children) Hospital- Sher-e-Bangla Nagar, Dhaka-1207,Bangladesh, Telephone- 88 02 55059051-60, Email- dhakashishu2010@gmail.com"
            if name == "Dr. MR Khan Shishu hospital & Institute of Child Health":
                message = "Here is the Address: Dr. MR Khan Shishu hospital & Institute of Child Health-  6/2 Section-02, Dhaka 1216 ,Telephone- +880 2-9023894, Mobile (Hotline)- 9023894, Email- drmrkhanshishuhospital@gmail.com,"
            if name == "Paediatric-Neonatal & General Hospital Limited":
                message = "Here is the Address: Paediatric-Neonatal & General Hospital Limited- 4, 4A Zakir Hosain Rd, Dhaka 1207 Telephone- 9138107,9138108, Mobile (Hotline)- 01818-890614, Email- http://www.dpnghospital.com, "


        dispatcher.utter_message(text=message)

        return []

# Doctors_search_by_name
class ActionDoctorsSearchByName(Action):

    def name(self) -> Text:
        return "action_doctors_search_by_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'Doctor_name':
                name = e['value']
            if name == "Dr. Mohammad Zakir Hossain":
                message = "Here are the information: Dr. Mohammad Zakir Hossain,MBBS, FCPS (Medicine), MD (Cardiology) ,Medicine & Cardiology Specialist, Consulting Hour: 7:00 PM to 9:00 PM, (Friday Closed)  "
            elif name == "Dr. Nurul Alam Talukder":
                message = "Here are the information: Dr. Nurul Alam Talukder, MBBS (DMC), MCPS (Medicine), D. Card, Cardiologist & medicine Specialist, Head of Dept. of Cardiology, Northern International Medical college Hospital, dhanmondi, Dhaka.,Consulting Hour: 6:00 PM to 8:30 PM, (Friday & Govt. Holiday Closed), "
            elif name == "Dr. Sirajul Haque":
                message = " Here are the information: Dr. Sirajul Haque, BSMMU, Shahbagh, Dhaka, Ex-Professor, NICVD, Dhaka,Ex-Director, NCCRF/HD, Dhaka. Anwar Khan Modern Medical College, Dhaka, Chamber phone: 01746711581 (A. Mojid) "
            elif name == "Dr. Azizul Bari":
                message = " Here are the information: Dr. Azizul Bari, MBBS, FCPS (Medicine), D-Card, Training Cardiology, Madras, India., Degree MBBS, FCPS (Medicine), D-Card, Training Cardiology, Madras, India. Visit Time 6.00 PM to 8.00 PM Saturday to Wednesday,"
            elif name == "Dr. Md. Arif Hossain":
                message = "Here are the information: Dr. Md. Arif Hossain, BCS (Health), MD (Cardiology-BSMMU) Clinical and Interventional Cardiologist & Medicine Specialist Consultant, Degree MBBS, MD (Cardiology) "
            elif name == "Dr. Khalifa Mahmud Tarik":
                message = "Here are the information: Dr. Khalifa Mahmud Tarik- MBBS (Dhaka), MS (CTS), Consultant, Cardiac Surgery. CABG and Congenital cardiac surgery both in adult and child. Phone: 10633, +8809666700100,  "
            elif name == "Dr. Md. Shaukat Ali":
                message = "Here are the information: Dr. Md. Shaukat Ali-  MBBS, FCPS (Surgery), MS (Cardiovascular & Thoracic Surgery),Clinical Fellow (NUH, Singapore). Phone: 10633, +8809666700100 "
            elif name == "Dr. Md. Lokman Hossain":
                message = "Here are the information: Dr. Md. Lokman Hossain-Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: 9am to 12pm & 5pm to 8pm(Closed: Friday), Contact Number: 10606 "
            elif name == "Dr. Amirul Islam Bhuyan":
                message = "Here are the information: Dr. Amirul Islam Bhuyan-,Address: House # 6, Road # 4, Dhanmondi, Dhaka, Contact Number: 10606 "
            elif name == "Dr. Nurun Nahar Fatema Begum":
                message = "Here are the information: Dr. Nurun Nahar Fatema Begum-Pediatrics Cardiologist. Address: House # 6, Road # 4, Dhanmondi, Dhaka,Visiting Hour: 4pm to 6.30pm (Closed: Friday), Contact Number: 10606.  "
            elif name == "Dr. Akhter Hamid Parvez":
                message = "Here are the information: Dr. Akhter Hamid Parvez-Cardiovascular & Thoracic Surgeon, Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: Unknown. Please call to know visiting hour, Contact Number: 10606 "
            elif name == "Dr. Arun Kumar Sharma":
                message = "Here are the information: Dr. Arun Kumar Sharma-Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: 9am to 1pm & 5pm to 10pm (Closed: Friday). Contact Number: 10606 "
            elif name == "Dr. Kamal Pasha":
                message = "Here are the information: Dr. Kamal Pasha-Interventional Cardiologist, Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616 "
            elif name == "Dr. SM Shahedul Amin Robin":
                message = "Here are the information: Dr. SM Shahedul Amin Robin-Cardiology Specialist, Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616.  "
            elif name == "Dr. Asif Manwar":
                message = " Here are the information: Dr. Asif Manwar- Cardiology Specialist. Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616. "
            elif name == "Dr. Nirmal Kanti Dey":
                message = "Here are the information: Dr. Nirmal Kanti Dey-Cardiac Surgeon, Address: House # 68, Road # 15/A, Dhanmondi, Dhaka,  Visiting Hour: 6pm to 9pm (Sat, Mon & Wednesday),  Contact Number: +8801823039800 "
            elif name == "Dr. Md. Zakir Hossain":
                message = "Here are the information: Dr. Md. Zakir Hossain-Cardiac Surgery Specialist. Address: House # 68, Road # 15/A, Dhanmondi, Dhaka, Visiting Hour: 9am to 5pm (Closed: Friday), Contact Number: +8801823039800.  "
            elif name == "Dr. Rakibul Hasan Apu":
                message = "Here are the information: Dr. Rakibul Hasan Apu- Cardiac Surgery Specialist. Address: House # 68, Road # 15/A, Dhanmondi, Dhaka, Visiting Hour: 2.30pm to 6pm (Sunday, Tuesday and Thursday), Contact Number: +8801823039800.  "
            elif name == "Dr. Fatema Begum":
                message = " Here are the information: Dr. Fatema Begum-Senior Consultant , Address: Plot # 15, Road # 71, Gulshan, Dhaka, Contact Number: 10666, Tel: +88 02 8836444, +88 02 8836000, Email: info@uhlbd.com"
            elif name == "Dr. Rezaul Hassan":
                message = "Here are the information: Dr. Rezaul Hassan- Cardiac Surgeon, Address: Plot # 15, Road # 71, Gulshan, Dhaka, Contact Number: 10666, Tel: +88 02 8836444, +88 02 8836000,  Email: info@uhlbd.com "
            elif name == "Dr. A. M. Shafique":
                message = "Here are the information: Dr. A. M. Shafique- Cardiology Specialist Address: Plot # 15, Road # 71, Gulshan, Dhaka, Contact Number: 10666,Tel: +88 02 8836444, +88 02 8836000,  Email: info@uhlbd.com "
            elif name == "PROF. Dr. M.A.K. Azad Chowdhury":
                message = "Here are the information: PROF. Dr. M.A.K. Azad Chowdhury,  MBBS, DCH, MRCP (UK), RCP (IRE), FRCP (EDIN), FCPS,  Prof. & Head, Deptt. of neonatology, Dhaka Shishu Hospital, Sher-e-Bangla nagor, Dhaka , Secretrary general, Bangladesh Paediatric Association, Consulting Hour: 5:00 PM to 9:00 PM, (Friday Closed) "
            elif name == "Prof. Chowdhury Md. Haider Ali":
                message = "Here are the information: Prof. Chowdhury Md. Haider Ali, MBBS, (DMC), DCH (Dublin), DCH, RCP & S (Irland), MD (Paed-Bangladesh Institute of Child Health), E-mail: Drcmhaider@yahoo.com, Mobile: 01683317564, Consulting Hour: 10:00 PM to 12:00 PM, (Friday Closed) "
            elif name == "Dr. Sultan Ahmed":
                message = "Here are the information: Dr. Sultan Ahmed , MBBS, DCH (Ireland), Child Specialist, Director & Ex-Chairman, Consultant, paediatrics, Cell: 01713039255 "
            elif name == "Dr. Mohammad Abdul Hai":
                message = "Here are the information: Dr. Mohammad Abdul Hai, MBBS, DCH (DU), FRSH (UK). Ass. Prof. (Child Health), Ex-Registrar , Dhaka Shishu Hospital,  Mobile: 01713060034 , Consulting Hour: Everyday: 11:00AM To 1:30 PM, Every Friday: 5:00AM To 9:00 PM. "
            elif name == "Dr. Kazi Md. Noor-Ul Ferdous":
                message = "Here are the information: Dr. Kazi Md. Noor-Ul Ferdous- MBBS, MS (Pediatric Surgery). Assistant Professor,  Neonatal & Pediatric Surgery Department,  Dhaka Shishu Hospital, Sher-e-Bangla Nagar, Dhaka,  Clinical Fellow in pediatric Laparoscopy. Queen Mary Hospital, Hong Kong,  Cell: 01711322487, Consulting Hour: 6:30 PM to 8:30 PM(Friday Closed).  "
            elif name == "Dr. Mahbubul Alam":
                message = "Here are the information: Dr. Mahbubul Alam, Consulting Address:Dhaka Central Consultation & Diagnostic Center, 4/ka, Ring Road, Shyamoli, Dhaka-1207.  Room No: 605,  Phone: 02 9145808-9,, Mob: 01746344179. Consulting Sessions: 7:30 PM to 9:00 PM "
            elif name == "Dr. Ahmed Zahid Hossain":
                message = "Here are the information: Dr. Ahmed Zahid Hossain- MBBS (Dhaka), MPH (Epidemiology), MS (Pediatric Surgery),  Phone: 10633, +8809666700100 "
            elif name == "Dr. Amina Akter":
                message = "Here are the information: Dr. Amina Akter- Child Kidney Specialist. Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: 9am to 1pm & 6pm to 10pm (Closed: Friday),  Contact Number: 10606 "
            elif name == "Dr. Musrat Rahman Deeba":
                message = "Here are the information: Dr. Musrat Rahman Deeba- Pediatric Surgery Specialist. Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Visiting Hour: Unknown. Please call to know visiting hour,, Contact Number: 10616.  "
            elif name == "Dr. Mahmuda Zaman":
                message = " Here are the information: Dr. Mahmuda Zaman-Child Cancer Specialist. Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka,  Contact Number: 10616"
            elif name == "Dr. ABM Abdus Salam":
                message = "Here are the information: Dr. ABM Abdus Salam- Pediatric Cardiology Specialist, Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka. Contact Number: 10616.  "
            elif name == "Dr. Lutfun Nahar Begum":
                message = " Here are the information: Dr. Lutfun Nahar Begum- Neonatal & Pediatrics Specialist , Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616. "
            elif name == "Dr. Rumana Choudhury":
                message = " Here are the information: Dr. Rumana Choudhury- Child Specialist. Address: House # 68, Road # 15/A, Dhanmondi, Dhaka, Visiting Hour: 9am to 4pm (Closed: Friday), Contact Number: +8801823039800."
            elif name == "Dr. Tahmina Karim":
                message = "Here are the information: Dr. Tahmina Karim- Child Specialist. Address: House # 68, Road # 15/A, Dhanmondi, Dhaka, Visiting Hour: 6pm to 9pm (Closed: Friday), Contact Number: +8801823039800.  "
            elif name == "Dr. Shahin Akter":
                message = "Here are the information: Dr. Shahin Akter- Pediatrics & Neonatal Specialist, Address: House # 68, Road # 15/A, Dhanmondi, Dhaka.  Visiting Hour: 6pm to 8pm (Closed: Friday),  Contact Number: +8801823039800 "
            elif name == "Dr. Kaniz Hasina":
                message = "Here are the information: Dr. Shahin Akter- Consultant,  Paediatric Surgery,  Address: Plot # 15, Road # 71, Gulshan, Dhaka.  Contact Number: 10666,.  Tel: +88 02 8836444, +88 02 8836000,  Email: info@uhlbd.com "
            elif name == "Dr. Prof. Md. Salim Shakur PhD":
                message = "Here are the information: Dr. Prof. Md. Salim Shakur PhD- Senior Consultant.Paediatrics,  Address: Plot # 15, Road # 71, Gulshan, Dhaka. Contact Number: 10666, Tel: +88 02 8836444, +88 02 8836000 , Email: info@uhlbd.com.  "
            elif name == "Prof. Dr. Md. Ehteshamul Hoque":
                message = "Here are the information: Prof. Dr. Md. Ehteshamul Hoque- Cancer Specialist (Radiotherapy), Clinical Oncologist. Professor, Anwer Khan Modern Medical College & Hospital & Consultant, City Hospital  Ltd. phone: 01711673550 "
            elif name == "Dr. M Safiul Alam":
                message = "Here are the information: Dr. M Safiul Alam- Consulting Address: Dhaka Central Diagnostic & Imaging Center, Address: 38/1, Ring Road, Shyamoli, Dhaka-1207. Phone: 02 58157532-4, Mobile: 01622446661-2. Consulting Sessions: 6:00 PM to 9:00 PM"
            elif name == "Dr. Qamruzzaman Chowdhury":
                message = "Here are the information: Dr. Qamruzzaman Chowdhury- Specialization Chemotherapy. Immunotherapy, Palliative Care , Radiation Therapy (IMRT, 3DCRT), Brachytherapy,  Phone: 10633, +8809666700100.  "
            elif name == "Dr. Ferdous Ara Begum":
                message = "Here are the information: Dr. Ferdous Ara Begum- MBBS DCH (Diploma In Child Health), (BICH) MD (Medical Oncology),  Phone: 10633, +8809666700100 "
            elif name == "Dr. Md. Arifur Rahman":
                message = "Here are the information: Dr. Md. Arifur Rahman- MBBS FCPS (Radiotherapy). Associate Consultant, Oncology & Radiotherapy,  Phone: 10633, +8809666700100.  "
            elif name == "Dr. A.F.M. Kamal Uddin":
                message = "Here are the information: Dr. A.F.M. Kamal Uddin- Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: 6pm to 10pm (Closed: Friday), Contact Number: 10606 "
            elif name == "Dr. Qazi Mushtaq Hussain":
                message = "Here are the information: Dr. Qazi Mushtaq Hussain- Address: House # 6, Road # 4, Dhanmondi, Dhaka, Visiting Hour: 6pm to 9pm (Closed: Thursday & Friday). Contact Number: 10606.  "
            elif name == "Dr. Arunangshu Das":
                message = "Here are the information: Dr. Arunangshu Das- Cancer Specialist Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616 "
            elif name == "Dr. Md. Salim Reza":
                message = "Here are the information: Dr. Md. Salim Reza- Cancer Specialist, Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka, Contact Number: 10616 "
            elif name == "Prof. Syed Md. Akram Hussain":
                message = "Here are the information: Prof. Syed Md. Akram Hussain- Clinical Oncologist & Radiotherapist, Address: 8/F, Kazi Nuruzzaman Road, West Panthapath, Dhaka. Contact Number: 10616. "
            elif name == "Prof. Dr. Zafor Md. Masum":
                message = "Here are the information: Prof. Dr. Zafor Md. Masum- Cancer Specialist, Address: House # 68, Road # 15/A, Dhanmondi, Dhaka, Visiting Hour: 2.30pm to 6pm (Everyday), Contact Number: +8801823039800 "
            elif name == "Dr. Rashid Un Nabi":
                message = "Here are the information: Dr. Rashid Un Nabi- Senior Consultant Radiation Oncology, Address: Plot # 15, Road # 71, Gulshan, Dhaka, Contact Number: 10666, Tel: +88 02 8836444, +88 02 8836000 Email: info@uhlbd.com "
            elif name == "Dr. Ashim Kumar Sengupta":
                message = "Here are the information: Dr. Ashim Kumar Sengupta- Consultant, Clinical and Radiation Oncology,  Address: Plot # 15, Road # 71, Gulshan, Dhaka,  Contact Number: 10666,, Tel: +88 02 8836444, +88 02 8836000, Email: info@uhlbd.com "
            elif name == "Prof. Dr. M Touhidul Haque":
                message = "Here are the information: Prof. Dr. M Touhidul Haque , Cardiology Specialist, Bangladesh Medical College & Hospital, Qualification -,BBS, MS (Cardiology), Chamber- Ibn Sina Diagnostic Center, Dhanmondi,  Address - House # 48, Road # 9/A, Dhanmondi, Dhaka – 1209, Visiting hour-  6pm to 11pm (Closed: Friday), Contact Number- +88029126625 "
            elif name == "Prof. Dr. Ashok Datta":
                message = "Here are the information: Prof. Dr. Ashok Datta Cardiology Specialist  National Heart Foundation Hospital, Qualification -MBBS, MD (Cardiology), FACC (USA), Chamber- Popular Diagnostic Center, Uttara, Address - House # 21, Road # 7, Sector # 4, Uttara, Dhaka (Unit 01), Visiting hour-  Everyday (Time Unknown), Contact Number- +8809613787805 "
            elif name == "Dr. Mohsin Ahmed":
                message = "Here are the information: Dr. Mohsin Ahmed, Cardiologist & Medicine Specialist,  Dhaka Medical College & Hospital; Qualification -MBBS, MCPS (Medicine), MD (Cardiology), FIC, FACC; Chamber- Ibn Sina Diagnostic Center, Doyagonj ; Address - 28, Hut Lane, Doyagonj, Gandaria, Dhaka. Visiting hour-   8pm to 11pm (Closed: Friday); Contact Number- +8801878115751.  "
            elif name == "Prof. Dr. Toufiqur Rahman Faruque  ":
                message = "Here are the information:  Prof. Dr. Toufiqur Rahman Faruque. Cardiology & Medicine Specialist; National Institute of Cardiovascular Diseases. Qualification -MBBS, MD (Cardiology), FCPS (Medicine), FACC (USA), FESC (EU). Chamber-Popular Diagnostic Center, Shantinagar ; Address - 4, Building # 15, Shantinagar, Dhaka (Unit 02) ; Visiting hour-  3pm to 6pm (Closed: Friday).Contact Number- +8809613787803.  "
            elif name == "Dr. Dhiman Banik":
                message = "Here are the information:    Dr. Dhiman Banik , Cardiology & Medicine Specialist; National Institute of Cardiovascular Diseases. Qualification -MBBS, MD (Cardiology), FCPS (Medicine), FACC (USA), FESC (EU)Chamber- Address - Popular Diagnostic Center, Shantinagar. Visiting hour-  3pm to 6pm (Closed: Friday). Contact Number- +8809613787803.  "
            elif name == "Prof. Dr. Md. Abdul Mannan":
                message = "Here are the information:  Prof. Dr. Md. Abdul Mannan. Pediatric & Neonatology Specialist, Bangabandhu Sheikh Mujib Medical University Hospital. Qualification -MBBS, FCPS, MD (Pediatric), MD (Neonatology), NUH (Singapore). Chamber- Labaid Specialized Hospital, Dhanmondi. Address - House # 6, Road # 4, Dhanmondi, Dhaka. Visiting hour-  6pm to 9.30pm (Friday: 10am to 12pm). Contact Number- 10606.  "
            elif name == "Prof. Dr. Tahmina Begum":
                message = "Here are the information:  Prof. Dr. Tahmina Begum. Child Specialist. Birdem General Hospital. Qualification - MBBS, FCPS (Child), MD, MMEd (UK). Chamber- Medinova Medical Services, Malibagh. Address - Hosaf Tower, 6/9 Outer Circular Road, Malibagh, Dhaka. Visiting hour-  5pm to 8pm (Closed: Friday). Contact Number- +8801790118855 "
            elif name == "Dr. Gopen Kumar Kundu":
                message = "Here are the informatio:  Dr. Gopen Kumar Kundu. Child Neurology Specialist. Bangabandhu Sheikh Mujib Medical University Hospital. Qualification -MBBS, DCH, FCPS (Child), MD (Child Neurology). Chamber- Green Life Hospital, Dhaka .  Address - 32, Green Road, Dhanmondi, Dhaka – 1205. Visiting hour-  7pm to 9pm (Closed: Friday). Contact Number- +8801618800088.  "
            elif name == "Dr. Kaniz Fatema":
                message = "Here are the information:  Dr. Kaniz Fatema. Child Neurology Specialist . Bangabandhu Sheikh Mujib Medical University Hospital . Qualification -MBBS, FCPS (Child Neurology) . Chamber- Ibn Sina Diagnostic Center, Dhanmondi. Address - House # 48, Road # 9/A, Dhanmondi, Dhaka – 1209. Visiting hour-  6pm to 9pm (Closed: Tuesday & Friday) . Contact Number- +88029126625.  "
            elif name == "Prof. Dr. Jahangir Alam":
                message = "Here are the information: Prof. Dr. Jahangir Alam. Child Specialist . Dhaka Shishu Hospital . Qualification -MBBS, DCH, MCPS, FCPS (Children)  . Chamber- Popular Diagnostic Center, Shantinagar .Address - House # 11, Shantinagar, Dhaka (Unit 01) . Visiting hour-  8pm to 10pm (Closed: Friday). Contact Number- +8809613787803.  "
            elif name == "Prof.Dr. Md. Moarraf hossen":
                message = "Here are the information:  Prof.Dr. Md. Moarraf hossen. Cancer Specialist . Evercare Hospital, Dhaka . Qualification - MBBS, DMRT, FCPS (Radiotherapy) . Chamber- Evercare Hospital . Address - Plot # 81, Block # E, Bashundhara R/A, Dhaka . Visiting hour-  9am to 5pm (Sat to Thu) . Contact Number- 10678.  "
            elif name == "Prof.Dr.sahana parvin":
                message = "Here are the information:  Prof.Dr.sahana parvin. Gyne Oncology Specialist . National Institute of Cancer Research & Hospital. Qualification - MBBS, DGO, FCPS (Gyne & Obs) . Chamber- Labaid Specialized Hospital, Dhanmondi . Address - House # 6, Road # 4, Dhanmondi, Dhaka. Visiting hour-  8pm to 10pm (Closed: Sunday, Tuesday and Thursday). Contact Number- 10606.  "
            elif name == "prof.Dr.Md. Mofazzel Hossain":
                message = "Here are the information:  Prof.Dr. Md. Moarraf hossen. Cancer Specialist . Evercare Hospital, Dhaka . Qualification - MBBS, DMRT, FCPS (Radiotherapy) . Chamber- Evercare Hospital . Address - Plot # 81, Block # E, Bashundhara R/A, Dhaka . Visiting hour-  9am to 5pm (Sat to Thu) . Contact Number- 10678.  "
            elif name == "prof.dr.swapan Bandyopadhyay":
                message = "Here are the information: prof.dr.swapan Bandyopadhyay. Cancer Specialist . Dhaka Medical College & Hospital . Qualification - MBBS, MD, MPHIL  . Chamber- Medinova Medical Services, Malibagh . Address - Hosaf Tower, 6/9 Outer Circular Road, Malibagh, Dhaka . Visiting hour-  6pm to 9pm (Closed: Friday) . Contact Number- +8801790118855.  "

        dispatcher.utter_message(text=message)

        return []

# doctors_search_by_cardiac
class ActionDoctorsSearchByCardiac(Action):

    def name(self) -> Text:
        return "action_doctors_search_by_cardiac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'problem_type':
                name = e['value']
            if name == "cardiac":
                message = "Here are some of the heart specialist . You can check out from here- Prof. Dr. M Touhidul Haque, Prof. Dr. Ashok Datta, Dr. Mohsin Ahmed, Prof. Dr. Toufiqur Rahman Faruque, Dr. Dhiman Banik, "

        dispatcher.utter_message(text=message)

        return []


# doctors_search_by_child
class ActionDoctorsSearchByChild(Action):

    def name(self) -> Text:
        return "action_doctors_search_by_child"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'problem_type':
                name = e['value']
            if name == "child":
                message = " Here are some of the Child specialist. You can check out from here- Prof. Dr. Md. Abdul Mannan, Prof. Dr. Tahmina Begum ,Dr. Gopen Kumar Kundu, Dr. Kaniz Fatema, Prof. Dr. Jahangir Alam,  "

        dispatcher.utter_message(text=message)

        return []



# doctors_search_by_cancer
class ActionDoctorsSearchByCancer(Action):

    def name(self) -> Text:
        return "action_doctors_search_by_cancer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global name, message
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'problem_type':
                name = e['value']
            if name == "cancer":
                message = "Here are some cancer specialists in Dhaka are- Dr.A.F.M. kamal Uddin, Prof.Dr. Md. Moarraf hossen, Prof.Dr.sahana parvin, prof.Dr.Md. Mofazzel Hossain, prof.dr.swapan Bandyopadhyay. "



        dispatcher.utter_message(text=message)

        return []
