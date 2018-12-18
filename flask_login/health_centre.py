from rating import Rating

class HealthCentre():
    def __init__(self, name, suburb, service_type, description,):
        self._name = name
        self._suburb = suburb
        self._service_type = service_type
        self._description = description
        self._doctors = []
        self._rating = Rating()

    def get_name(self):
        return self._name

    def get_suburb(self):
        return self._suburb

    def get_service_type(self):
        return self._service_type

    def get_description(self):
        return self._description

    def get_doctors(self):
        return self._doctors  # draft 1

    def get_average_rating(self):
        return self._rating.get_average()

    def record_rating(self, customer, score):
        self._rating.makeRating(customer, score)

    def isRated(self, customer):
        if self._rating.get_previous_rating(customer):
            return True
        return False

    def __str__(self):
        return 'name:' + self._name + '-suburb:' +self._suburb + '-service_type:' +self._service_type

    def add_doctor(self, doctor):
        #print(doctor)
        if doctor not in self._doctors:
            self._doctors.append(doctor)
            #print('    '  + str(self) + 'got' + str(doctor.get_name()))
            #print(self.get_doctors())

class HealthCentreManager():
    def __init__(self):
        self._health_centres = []

    def __str__(self):
        toreturn = []
        for hc in self._health_centres:
            toreturn.append(str(hc))
        return str(toreturn)
    
    def add_health_centre(self, name, suburb, service_type, description = ''):
        newHC = HealthCentre(name, suburb,service_type, description,)
        self._health_centres.append(newHC)

    def search_by_name(self, name): #returns HealthCentre on matches or None
        for hc in self._health_centres:
            if hc.get_name() == name:
                return hc
        return None
            
    def search_by_suburb(self, suburb):
        toReturn = []
        for hc in self._health_centres:
            if hc.get_suburb() == suburb:
                toReturn.append(hc)
        return toReturn

    def search_by_service_type(self, service_type):
        toReturn = []
        for hc in self._health_centres:
            if hc.get_service_type() == service_type:
                toReturn.append(hc)
        return toReturn

    @property
    def health_centres(self):
        return self._health_centres
