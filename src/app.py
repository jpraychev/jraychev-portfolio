import json
from datetime import datetime
from email_validator import validate_email
from flask import Flask, render_template, request
from utils import validate_string
from utils import get_last_commit_and_upstream_url
import constants
from google_recaptcha import ReCaptcha
from telegram import Bot

app = Flask(__name__)
recaptcha = ReCaptcha(app)
bot = Bot()

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html")

@app.route('/')
@app.route('/home/')
def home():
    if request.method == 'GET':
        with open(constants.HOME_PATH) as f:
            home_data = json.load(f)
        return render_template('home.html', context=home_data)

@app.route('/services/')
def services():
    if request.method == 'GET':
        with open(constants.SERVICES_PATH) as f:
            service_data = json.load(f)
        return render_template('services.html', context=service_data)

@app.route('/experience/')
def experience():
    if request.method == 'GET':
        with open(constants.EXPERIENCE_PATH) as f:
            experience_data = json.load(f)
        return render_template('experience.html', context=experience_data)

@app.route('/blog/')
def blog():
    if request.method == 'GET':
        return render_template('blog.html')

@app.route('/projects/')
def projects():
    if request.method == 'GET':
        with open(constants.PROJECT_PATH) as f:
            projects_data = json.load(f)
        return render_template('projects.html', context=projects_data)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    
    context = {
        'feedback_message' : '',
        'alert_type' : ''
    }

    try:
        with open(constants.CONTACT_PATH) as f:
            contact_data = json.load(f)
            num_of_objects = len(contact_data)
            idx = 1 if num_of_objects == 0 else num_of_objects + 1
    except (FileNotFoundError, json.JSONDecodeError):
        # FileNotFoundError - create the file if not there
        # json.JSONDecodeError - add {} to file if exists but empty
        with open(constants.CONTACT_PATH, 'w') as f:
            f.write(json.dumps({}))

    if request.method == 'GET':
        return render_template('contact.html', context=context)

    if request.method == 'POST':

        if not recaptcha.verify():
            context['feedback_message'] = "Suspicious of robot activities"
            context['alert_type'] = 'danger'
            return render_template('contact.html', context=context)

        timestamp_now = int(datetime.now().timestamp())
        
        try:
            form_data = {
                'name' : validate_string(request.form['name']),
                'email' : validate_email(request.form['email']).email,
                'subject' : validate_string(request.form['subject']),
                'message' : validate_string(request.form['message'])
            }
        except:
            context['feedback_message'] = "You've entered incorrect data"
            context['alert_type'] = 'danger'
            return render_template('contact.html', context=context)

        contact_data[idx] = form_data
        contact_data[idx]['time_of_posting'] = timestamp_now

        with open(constants.CONTACT_PATH, 'w') as f:
            f.write(json.dumps(contact_data))
        context['feedback_message'] = "Your message has been sent successfully!"
        context['alert_type'] = 'success'

        msg = f'Received message on {request.host_url} from {validate_string(request.form["name"])}'
        bot.send_msg(to='-628470117', msg=msg)
        return render_template('contact.html', context=context)

@app.context_processor
def context_variables():
    now = datetime.now()
    formatted_today = f'{now.year}/{now.month}/{now.day}'
    commit, upstream_url = get_last_commit_and_upstream_url('origin', 'main')
    
    return {
        'today' : formatted_today,
        'last_upstream_commit' : commit,
        'upstream_url' : upstream_url
    }

if __name__ == "__main__":
    
    app.run(
        host='127.0.0.1',
        port=5050,
        debug=True
    )