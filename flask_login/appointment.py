from datetime import *
class Appointment():
    _app_id = 0

    @staticmethod
    def get_new_app_id():
        Appointment._app_id += 1
        return Appointment._app_id

    def __init__(self, patient, health_provider, time, message): #HASUser, UASuser, string: matches the following format "%a %b %d %H:%M:%S %Y", refer to python time module
        self.health_provider = health_provider
        self.patient = patient
        self.time = time    #will result in time.struct_time object
        self.message = message
        self._note = None
        self._id = Appointment.get_new_app_id()

    def __str__(self):
        return 'doctor:'+ str(self.health_provider) + ' patient:' + str(self.patient) + ' time:' + str(self.time) + ' message:' + self.message

    def get_health_provider(self):
        return self.health_provider

    def get_patient(self):
        return self.patient
    
    def get_time(self):
        return self.time

    def take_note(self, note):
        self._note = note

    @property
    def note(self):
        return self._note

    @property
    def id(self):
        return self._id