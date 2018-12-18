import pytest

from app import app
from HASSystem import *
from health_centre import HealthCentreManager, HealthCentre
from HASUser import HASUser, HASUserMnanager, HealthProvider, Patient
from HASUser import *
from infoImporter import import_health_centres, import_patient, import_health_provider, import_workspace

from functools import wraps
from datetime import *

#init
hcMng = HealthCentreManager()
userMng = HASUserMnanager()
system = HASystem(userMng, hcMng, None)

import_health_centres(system.healthCentreMng)
import_patient(system.userMng)
import_health_provider(system.userMng)
import_workspace(system)

#user

def test_createUser():
    us_0 = User('abcde','12345678')
    assert(us_0._username == 'abcde' and us_0._password == '12345678')
  
def test_AssignID():
    us_0 = User('abcde','12345678')
    us_0.assign_ID(12321)
    assert(us_0.get_id() == 12321)

def test_authenticate():
    us_0 = User('abcde','12345678')
    us_0.assign_ID(12321)
    assert(us_0.authenticate('12345678'))
    assert(not us_0.authenticate('asdasddsa'))

#system

def test_search_hc_by_name():
    assert('Sydney Children Hospital' == system.search_health_centre_by_name_near_search('Sydney Children ')[0].get_name())

def test_search_hc_by_type():
    assert('Sydney Children Hospital' in [x.get_name() for x in system.search_health_centre_type_near_search('hosp')])

def test_search_hc_by_suburb():
    assert('UTS Health Service' == [x.get_name() for x in system.search_health_centre_suburb_near_search('Ulti')][0])

def test_search_hp_by_name():
    assert('toby@gmail.com' == [x.get_name() for x in system.search_health_provider_type_near_search('toby')][0])

#ratings
class TestRating(object):
    
    def setup_method(self):
        self.sample_pat_0 = Patient('pat0','pass','pat0')
        self.sample_pat_0.assign_ID(0)
        self.sample_pat_1 = Patient('pat1','pass','pat1')
        self.sample_pat_1.assign_ID(1)
        self.sample_doc_0 = HealthProvider('doc0', 'pass', 'doc0', 'just a doc')
        self.sample_doc_0.assign_ID(2)
        self.sample_hc_0 = HealthCentre('hos0','Sydney','Hospital','Just a hosptital')

    def test_succ_make_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        assert self.sample_hc_0.get_average_rating() == 10

    def test_succ_replace_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        self.sample_hc_0.record_rating(self.sample_pat_0, 3)
        assert self.sample_hc_0.get_average_rating() == 3

    def test_succ_mult_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        self.sample_hc_0.record_rating(self.sample_pat_1, 8)
        assert self.sample_hc_0.get_average_rating() == 9

    def test_empty_input_make_hc(self):
        self.setup_method()
        try:
            self.sample_hc_0.record_rating(self.sample_pat_0, None)
        except ValueError:
            assert(True)
        else:
            assert(False)
        
#appointment
datetime_format = "%Y-%m-%d:%H:%M"

def test_getHealthProvider():
    appointment_0 = Appointment('Patient_0', 'HealthProvider_0', datetime.strptime('2016-03-01:03:03', datetime_format) , 'Broken Leg')
    appointment_1 = Appointment('Patient_1', 'HealthProvider_1', datetime.strptime('2016-04-01:03:03', datetime_format), None)
    assert(appointment_0.get_health_provider()=='HealthProvider_0')
    assert(appointment_1.get_health_provider()=='HealthProvider_1')

def test_getPatient():
    appointment_0 = Appointment('Patient_0', 'HealthProvider_0', datetime.strptime('2016-03-01:03:03', datetime_format) , 'Broken Leg')
    appointment_1 = Appointment('Patient_1', 'HealthProvider_1', datetime.strptime('2016-04-01:03:03', datetime_format), None)
    assert(appointment_0.get_patient()=='Patient_0')
    assert(appointment_1.get_patient()=='Patient_1')

def test_getTime():
    appointment_0 = Appointment('Patient_0', 'HealthProvider_0', datetime.strptime('2016-03-01:03:03', datetime_format) , 'Broken Leg')
    appointment_1 = Appointment('Patient_1', 'HealthProvider_1', datetime.strptime('2016-04-01:03:03', datetime_format), None)
    assert(appointment_0.get_time().strftime(datetime_format)=='2016-03-01:03:03')
    assert(appointment_1.get_time().strftime(datetime_format)=='2016-04-01:03:03')