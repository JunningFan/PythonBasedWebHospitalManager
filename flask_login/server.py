from app import app
from HASSystem import *
from  health_centre import HealthCentreManager, HealthCentre
from HASUser import HASUser, HASUserMnanager, HealthProvider, Patient
from flask_login import login_user, logout_user,  current_user, LoginManager
from flask import redirect, url_for,request

from infoImporter import import_health_centres, import_patient, import_health_provider, import_workspace

from functools import wraps
from datetime import *

#configure HAS system

hcMng = HealthCentreManager()
userMng = HASUserMnanager()
login_manager = LoginManager()
login_manager.init_app(app)

system = HASystem(userMng, hcMng, login_manager)

#configure Flask-login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #print(current_user)
        if current_user is None or not current_user.is_authenticated:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return system.userMng.get_user(user_id)


#
#initialize users/health centres
import_health_centres(system.healthCentreMng)
import_patient(system.userMng)
import_health_provider(system.userMng)

import_workspace(system)
