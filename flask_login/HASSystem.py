from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class HASystem():
    def __init__(self, userMng, healthCentreMng, loginManager):
        self.userMng = userMng
        self.healthCentreMng = healthCentreMng
        self.loginMng = loginManager
    
    #user services
    def login_user(self, id):
        pass

    def assign_health_provider_to_health_centre(self, health_centre_name, health_provider_name):
        hc = self.healthCentreMng.search_by_name(health_centre_name)
        hp = self.userMng.get_user_by_name(health_provider_name, 'health_provider')
        if hc and hp:
            print(str(hc) + ' got '+ str(hp))
            hc._doctors.append(hp)

    #search services
    def search_health_centre_by_name_near_search(self, name):
        '''
        print(name)
        sortedByScore = []
        for hc in self.healthCentreMng.health_centres:
            sortedByScore.append([hc, fuzz.partial_ratio(hc.get_name(), name)])
        sortedByScore.sort(key=lambda x: x[1], reverse=True)
        toReturn = []
        for key_score_pair in sortedByScore:
            toReturn.append(key_score_pair[0])'''
        return sorted(self.healthCentreMng.health_centres, key = lambda x: fuzz.partial_ratio(x.get_name().lower(), name.lower()), reverse = True)

    def search_health_centre_suburb_near_search(self, suburb):
        return sorted(self.healthCentreMng.health_centres, key = lambda x: fuzz.partial_ratio(x.get_suburb().lower(), suburb.lower()), reverse = True)

    def search_health_centre_type_near_search(self, service_type):
        return sorted(self.healthCentreMng.health_centres, key = lambda x: fuzz.partial_ratio(x.get_service_type().lower(), service_type.lower()), reverse = True)
        
    def search_health_provider_type_near_search(self, name):
        return sorted(self.userMng.health_provider, key = lambda x: fuzz.partial_ratio(x.get_name().lower(), name.lower()), reverse = True)

    def search_patient_by_name(self, health_provider, patient_name):
        print([x.patient.get_name() for x in health_provider.get_appointment()])
        if patient_name in [x.patient.get_name() for x in health_provider.get_appointment()]:
            print('found patient')
            return self.userMng.get_user_by_name(patient_name, 'patient')
        return None

    def get_patient_appointment_by_app_id(self, patient_name, app_id):
        target_pat = self.userMng.get_user_by_name(patient_name, 'patient')
        print(str(target_pat) + "app_id: " + str(app_id))
        for app in target_pat.get_appointment():
            print(app.id)
            if app.id == int(app_id):
                print('app found')
                return app
            print('app not found')
        return None