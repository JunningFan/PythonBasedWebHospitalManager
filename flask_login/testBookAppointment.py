import pytest
from appointment import Appointment


def test_getHealthProvider(self):
    self.appointment_0 = Appointment('Patient_0', 'HealthProvider_0', 10:30:00, 'Broken Leg')
    self.appointment_1 = Appointment('Patient_1', 'HealthProvider_1', 21:00:00, None)
    assert(appointment_0.get_health_provider()=='HealthProvider_0')
    assert(appointment_1.get_health_provider()=='HealthProvider_1')

def test_getPatient(self):
    self.appointment_0 = Appointment('Patient_0', 'HealthProvider_0', 10:30:00, 'Broken Leg')
    self.appointment_1 = Appointment('Patient_1', 'HealthProvider_1', 21:00:00, None)
    assert(appointment_0.get_patient()=='Patient_0')
    assert(appointment_1.get_patient()=='Patient_1')

def test_getTime(self):
    self.appointment_0 = Appointment('Patient_0', 'HealthProvider_0', 10:30:00, 'Broken Leg')
    self.appointment_1 = Appointment('Patient_1', 'HealthProvider_1', 21:00:00, None)
    assert(appointment_0.get_time()==10:30:00)
    assert(appointment_0.get_time()==21:00:00)
