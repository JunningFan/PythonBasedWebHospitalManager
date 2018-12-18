import csv

def remove_apostrophe_and_leading_space(string):
    toRemove = "'"
    for char in toRemove:
        string = string.replace(char, "")
    if string[0] == ' ':
        return string[1:] 
    return string

def import_health_centres(hcMng):
    COLUMNS = [
        'type',
        'ignore',
        'name',
        'ignore_1',
        'suburb'
    ]
    with open('health_centres.csv') as f:
        reader = csv.DictReader(f, fieldnames = COLUMNS)
        for row in reader:
            #print('name:{}, type:{}, suburb:{}'.format(remove_apostrophe_and_leading_space(row['name']), remove_apostrophe_and_leading_space(row['type']), remove_apostrophe_and_leading_space(row['suburb'])))
            hcMng.add_health_centre(remove_apostrophe_and_leading_space(row['name']), remove_apostrophe_and_leading_space(row['suburb']), remove_apostrophe_and_leading_space(row['type']))

def import_patient(userMng):
    COLUMNS = [
        'username',
        'password'
    ]
    with open('patient.csv') as f:
        reader = csv.DictReader(f, fieldnames = COLUMNS)
        for row in reader:
            #print('username:{}, password:{}, name:{}'.format(remove_apostrophe_and_leading_space(row['username']), remove_apostrophe_and_leading_space(row['password']), remove_apostrophe_and_leading_space(row['username'])))
            userMng.add_patient(remove_apostrophe_and_leading_space(row['username']), remove_apostrophe_and_leading_space(row['password']), remove_apostrophe_and_leading_space(row['username']))
        
def import_health_provider(userMng):
    COLUMNS = [
        'username',
        'password',
        'profile'
    ]
    with open('provider.csv') as f:
        reader = csv.DictReader(f, fieldnames = COLUMNS)
        for row in reader:
            #print('username:{}, password:{}, profile:{}'.format(remove_apostrophe_and_leading_space(row['username']), remove_apostrophe_and_leading_space(row['password']), remove_apostrophe_and_leading_space(row['profile'])))
            userMng.add_health_provider(remove_apostrophe_and_leading_space(row['username']), remove_apostrophe_and_leading_space(row['password']), remove_apostrophe_and_leading_space(row['profile']))

def import_workspace(system):
    COLUMNS = [
        'health_provider',
        'health_centre'
    ]
    with open('provider_health_centre.csv') as f:
        reader = csv.DictReader(f, fieldnames = COLUMNS)
        for row in reader:
            print('hc:{}, hp:{}'.format(row['health_centre'], row['health_provider']))  
            print(system.healthCentreMng.search_by_name(row['health_centre']))   
            system.assign_health_provider_to_health_centre(row['health_centre'], row['health_provider'])
            pass
        #system.healthCentreMng.search_by_name('USYD Health Service').add_doctor(system.userMng.get_user(4))
