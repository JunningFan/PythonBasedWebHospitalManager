import pytest
from HASUser import HASUser, HealthProvider

def test_getProfilePage:
    self.doc_0 = HealthProvider('Username_0', 'Password_0', 'Doc 0', 'Profile 0')
    self.doc_1 = HealthProvider('Username_1', 'Password_1', 'Doc 1', 'Profile 1')
    assert(doc_0.get_profile()=='Profile 0')
    assert(doc_0.get_profile()=='Profile 1')
