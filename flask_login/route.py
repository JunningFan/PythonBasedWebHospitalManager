from app import app
from server import *
from flask import url_for, redirect, render_template, request, flash

@app.route('/', methods = ['GET', 'POST'])
def index():
    if current_user.is_authenticated == False:
        return redirect('login',302)
    if request.method == 'GET':
        return render_template('mainpage.html', user = current_user, method = request.method)
    else:
        if current_user.get_identity() == 'patient':
            hcResult = []
            hpResult = None
            if request.form['name']:
                #hcResult.append(system.healthCentreMng.search_by_name(request.form['name']))
                #print(request.form['name'])
                hcResult = system.search_health_centre_by_name_near_search(request.form['name'])
            elif request.form['suburb']:
                hcResult = system.search_health_centre_suburb_near_search(request.form['suburb'])
            elif request.form['service_type']:
                hcResult = system.search_health_centre_type_near_search(request.form['service_type'])
            elif request.form['health_provider_name']:
                hpResult = system.search_health_provider_type_near_search(request.form['health_provider_name'])
            return render_template('mainpage.html', user = current_user,\
            method = request.method, hcResult = hcResult, hpResult = hpResult)
        else:
            if request.form['name']:
                patientResult = system.search_patient_by_name(current_user, request.form['name'])
                return render_template('mainpage.html', user = current_user,\
                method = request.method, patientResult = patientResult)
        return render_template('mainpage.html', user = current_user, method = request.method)
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'GET'):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html',  user = current_user)
    else:
        user = system.userMng.login(request.form['username'], request.form['password'])
        if user != None:
            flash('Logged in successfully.')
            login_user(user)
            return redirect(request.args.get("next") or url_for('index'))
        else:
            flash('Invalid account-password pair.')
            return redirect(url_for('login'),302)
    return 'LOGIN ERROR'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'),302) 

@app.route('/myPage', methods=['GET','POST'])
@login_required
def myPage():
    if request.method == 'POST':
        try:
            if request.form['note']:
                target_app = system.get_patient_appointment_by_app_id(request.form['patient_name'], request.form['target_app_id'])
                target_app.take_note(request.form['note'])
            else:
                return render_template('/myPage.html',\
                user = current_user, \
                identity = current_user.get_identity() ,appointments = current_user.get_appointment(), errorMsg = 'Note cannot be empty')
        except AttributeError:
            return render_template('/myPage.html',\
                user = current_user, \
                identity = current_user.get_identity() ,appointments = current_user.get_appointment(), errorMsg = 'Appointment info not synced, Please try again')
    return render_template('/myPage.html',\
        user = current_user, \
        identity = current_user.get_identity() ,appointments = current_user.get_appointment())

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if userMng.get_user(int(request.args.get('id'))).get_identity() == 'health_provider':
        target_provider = userMng.get_user(int(request.args.get('id')))
        if request.method == 'POST':
            if request.form['rating']:
                target_provider.record_rating(current_user, int(request.form['rating']))
        return render_template('profile.html', \
        user = current_user, \
        hp = target_provider)
    else:
        return redirect(url_for('index')) #todo



@app.route('/health_centre_profile', methods=['GET','POST'])
@login_required
def health_centre_profile():
    targetCentre =  system.healthCentreMng.search_by_name(request.args.get('name'))
    #print(request.args.get('name'))
    if targetCentre:
        if request.method == 'POST':
            if request.form['rating']:
                targetCentre.record_rating(current_user, int(request.form['rating']))
            else:
                return render_template('health_centre_profile.html', \
                    user = current_user, \
                    health_centre = targetCentre, errorMsg = 'Please enter a correct rating as an integer between 1 to 10')
        services = []
        for hp in targetCentre.get_doctors():
            if hp.get_profile() not in services:
                services.append(hp.get_profile())
                print(services)
        return render_template('health_centre_profile.html', \
            user = current_user, \
            health_centre = targetCentre, services = services)
    else:
        return redirect(url_for('index'))
            

@app.route('/appointment', methods = ['GET','POST'])
@login_required
def appointment():
    try:
        targetHP = system.userMng.get_user(int(request.args.get('id')))
    except:
        return redirect(url_for('index'))

    if (not targetHP) or targetHP.get_identity() != 'health_provider':
        return redirect(url_for('index'))

    date_format = "%Y-%m-%d"
    today = datetime.now().strftime(date_format)    
    if request.method == 'GET': 
        return render_template('/appointment.html', user = current_user, \
        health_provider_name = targetHP.get_name(),  today = today, pick_date = True)
    else:
        if 'check' in request.form:
            try:
                return render_template('/appointment.html', user = current_user, \
                    health_provider_name = targetHP.get_name(),  today = today, pick_date = False, time_slots = targetHP.get_avaliable_time_slot(request.form['date']), date = request.form['date'])
            except:
                return render_template('/appointment.html', user = current_user, \
                    health_provider_name = targetHP.get_name(),  today = today, pick_date = True)
        else:
            try:
                datetime_format = "%Y-%m-%d:%H:%M"
                #print(request.form['date'] +'-'+request.fstrftime("%Y-%m-%d %H:%M:%S")orm['time'], datetime_format)
                time = datetime.strptime(request.form['date'] +':'+request.form['time'], datetime_format)
                if time.strftime("%H:%M") in targetHP.get_avaliable_time_slot(request.form['date']):
                    current_user.apply_appointment(system.userMng.get_user(int(request.args.get('id'))), time, request.form['message'])
                else: 
                    return redirect(url_for('myPage'))
            except KeyError:
                return render_template('/appointment.html', user = current_user, \
                health_provider_name = targetHP.get_name(), errorMsg='Please pick a time slot')
            except AttributeError:
                return render_template('/appointment.html', user = current_user, \
                health_provider_name = targetHP.get_name(), errorMsg='Doctor account cannot be used to make appointments')
            return redirect(url_for('myPage'))

