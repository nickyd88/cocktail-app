import datetime
from flask import Flask, render_template, redirect, url_for, request
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
from data_functions import store_time, fetch_times, getUsers, User
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from data_functions import getIngredients
from config import Config
import copy

app = Flask(__name__)

 ## Routes go here
firebase_request_adapter = requests.Request()
userlist = getUsers()
login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object(Config)

@app.route("/", methods = ["GET", "POST"])
def root():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if request.method == 'POST':
        username = request.form['username']
        user = User(username)
        #print(username)
        login_user(user)
        return redirect(url_for('userpage'))
    else:
        return render_template('login.html', userlist = userlist)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if request.method == 'POST':
        username = request.form['username']
        user = User(username)
        #print(username)
        login_user(user)
        return redirect(url_for('userpage'))
    else:
        return render_template('login.html', userlist = userlist)

@app.route('/user', methods = ['GET', 'POST'])
@login_required
def userpage():

    ingredients = {}
    for i in getIngredients():
        ingredients[i] = {'stocked': False, 'notes': ''}

    if request.method == 'POST':
        formdict = request.form.to_dict()
        for i in formdict.keys():
            if i in ingredients.keys():
                ingredients[i]['stocked'] = True
            if i.endswith('.notes'):
                if formdict[i] != '':
                    ingredients[i[:-6]]['notes'] = formdict[i]



        return render_template('user.html', user=current_user, ingredient_list = ingredients.keys())

    else:
        return render_template('user.html', user=current_user, ingredient_list = ingredients.keys())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('index')



## Run the thing

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)