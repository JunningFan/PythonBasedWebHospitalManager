class appointmentFailExecption(Exception):
    def __init__(self):
        self.message = 'asdsaadd'

a = []
a.append(None)
print(a)
def b():
    raise appointmentFailExecption()

try:
    a.append(b())
except appointmentFailExecption as exp:
    print(exp.message)
finally:
    pass
print(a)
