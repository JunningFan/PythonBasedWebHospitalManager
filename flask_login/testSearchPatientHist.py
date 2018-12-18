import pytest
from .HASUser import *
from appointment import Appointment

def test_getEmptyPatientHist():
    patient_0 = HASUser('Username_0', 'Password_0', 'patient', 'Name_0')
    assert len(patient_0._appointments)==0
    return 'No appointments in patient history.'

def test_getPatientHist():
    patient_1 = HASUser('Username_1', 'Password_1', 'patient', 'Name_1')
    patient_1._appointments = [Appointment('Name_1', 'Doc_1', '14:00/03/02/16', 'Fever'), Appointment('Name_1', 'Doc_0', '10:30/03/09/17', 'Flu')]
    assert len(patient_1._appointments)!=0,"Error! Could not find patient history."
    assert(patient_1.get_appointment() == patient_1._appointments)
