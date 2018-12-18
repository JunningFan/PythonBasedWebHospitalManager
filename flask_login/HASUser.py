from user import User, UserManager
from appointment import Appointment
from rating import Rating

from abc import abstractclassmethod
from datetime import *


class HASUser(User):
    def __init__(self, username, password, identity, name):
        self._identity = identity
        self._name = name
        self._appointments = []
        User.__init__(self, username, password)
    
    def get_identity(self):
        return self._identity
    
    def get_name(self):
        return self._name

    def get_appointment(self):
        return self._appointments

    def __str__(self):
        return User.__str__(self) + ' ' + self._identity

class HealthProvider(HASUser):
    def __init__(self, username, password, name, profile):
        HASUser.__init__(self, username, password, 'health_provider', name)
        self._profile = profile
        self._healthCentre = []
        self._rating = Rating()
    
    def make_appointment(self, patient, time, message):
        new_appointment = Appointment(patient, self, time, message)
        self._appointments.append(new_appointment)
        self._appointments.sort(key=lambda x: x.time, reverse=False) # sort appointments
        return new_appointment

    def get_avaliable_time_slot(self, date):
        avaliable_slots = []
        for hour in range(0,24):
            for minute in [00, 30]:
                slot = datetime.strptime(date + ' ' + str(hour) + ':' + str(minute) , '%Y-%m-%d %H:%M')
                if slot.strftime("%Y-%m-%d %H:%M") not in [x.time.strftime("%Y-%m-%d %H:%M") for x in self.get_appointment()]:
                    avaliable_slots.append(slot.strftime("%H:%M"))
        return avaliable_slots

    def get_health_centre(self):
        pass    #todo
    
    def get_profile(self):
        return self._profile

    def get_average_rating(self):
        return self._rating.get_average()

    def record_rating(self, customer, score):
        self._rating.makeRating(customer, score)

    def isRated(self, customer):
        if self._rating.get_previous_rating(customer):
            return True
        return False


    def __str__(self):
        return HASUser.__str__(self) +  ' ' + str(self._healthCentre) 

class Patient(HASUser):
    def __init__(self, username, password, name):
        HASUser.__init__(self, username, password, 'patient', name)
    
    def apply_appointment(self, health_provider, time, message):
        self._appointments.append(health_provider.make_appointment(self, time, message))
        self._appointments.sort(key=lambda x: x.time, reverse=False)

class HASUserMnanager(UserManager):
    def __init__(self):
        UserManager.__init__(self)
    
    def get_user_by_name(self, name, identity):
        #print(name+identity)
        for user in self._users.values():
            #print(user.get_name() + ' ' + user.get_identity())
            if user.get_name() == name and user.get_identity() == identity:
                print(user)
                return user
        return None
    
    def add_patient(self, username, password, name):
        self.add_user(Patient(username,password,name))
    
    def add_health_provider(self, username, password, profile):
        self.add_user(HealthProvider(username, password, username, profile))

    @property
    def patients(self):
        toReturn = []
        for user in self._users.values():
            if user.get_identity() == 'patient':
                toReturn.append(user)
        return toReturn

    @property
    def health_provider(self):
        toReturn = []
        for user in self._users.values():
            print(user)
            if user.get_identity() == 'health_provider':
                toReturn.append(user)
        return toReturn

if __name__ == '__main__':
    hp = HealthProvider(None,None,None,None)
    print(hp.get_avaliable_time_slot('2018-09-01'))
    hp.make_appointment(None,datetime.strptime('2018-09-01 08:30', '%Y-%m-%d %H:%M'), None)
    print(hp.get_avaliable_time_slot('2018-09-01'))
