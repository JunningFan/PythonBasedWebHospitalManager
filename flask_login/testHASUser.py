from .HASUser import *
import pytest

def test_getIdentity():
    doc = HealthProvider('a','b','c')
    pat = Patient('d','e','f')
    assert(doc.get_identity() == 'health_provider')
    assert(pat.get_identity() == 'patient')

def test_getName():
    doc = HealthProvider('a','b','c')
    pat = Patient('d','e','f')
    assert(doc.get_name() == 'c')
    assert(pat.get_name() == 'f')

def test_appointment():
    doc = HealthProvider('a','b','c')
    pat = Patient('d','e','f')
    expectedAppointment = Appointment(pat, doc, '13:05/09/02/2021')
    expectedAppointment2 = Appointment(pat, doc, '13:05/09/02/2021')
    pat.apply_appointment(doc, '13:05/09/02/2021')
    assert(True)