import pytest
from .user import *
#unit tests    

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

test_createUser()
test_AssignID()
test_authenticate()