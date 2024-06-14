import datetime
from flask import Flask, render_template, redirect, url_for, request, jsonify
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
from database import getUsers, getIngredients, getCocktails, getCocktailsFromDB, getRecipe, getFav, addRemoveFav
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from data_functions import getStock, createStockDictionary, deleteStock, entityJson, updateStock, User
from config import Config
import copy
import json
from gpt import getGPT

app = Flask(__name__)

 ## Routes go here
firebase_request_adapter = requests.Request()
userlist = getUsers()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"


app.config.from_object(Config)

@app.route("/", methods = ["GET", "POST"])
def root():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    logout_user()
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



@app.route('/user', methods = ['GET', 'POST'])
@login_required
def userpage():

    stock = getStock(current_user.username)

    if request.method == 'POST':
        formdict = request.form.to_dict()
        for i in stock.keys():
            if i in formdict.keys():
                stock[i]['stocked'] = True
            else:
                stock[i]['stocked'] = False
        for i in formdict.keys():
            if i.endswith('.notes'):
                if formdict[i] != '':
                    stock[i[:-6]]['notes'] = formdict[i]
                else:
                    stock[i[:-6]]['notes'] = ''

        updateStock(current_user.username, stock)

        sorted_stock = {}
        for item in getIngredients():
            sorted_stock[item] = stock[item]

        return render_template('user.html', user=current_user, stock = sorted_stock)

    else:
        sorted_stock = {}
        for item in getIngredients():
            sorted_stock[item] = stock[item]
        return render_template('user.html', user=current_user, stock = sorted_stock)



@app.route('/recipes')
@login_required
def recipepage():
    recipes = getCocktailsFromDB()
    stock = getStock(current_user.username)
    favlist = getFav(current_user.username)

    for rec in recipes.keys():
        recipes[rec]['stocked']=False
        have = []
        missing = ''
        need = set(recipes[rec]['ingredients'])

        for ing in recipes[rec]['ingredients']:
            try:
                if stock[ing]['stocked'] is True:
                    have.append(ing)
                else:
                    missing = missing + ing + ', '
            except KeyError:
                missing = missing + ing + ', '
            
        if len(missing)==0:
            recipes[rec]['stocked'] = True
            recipes[rec]['missing'] = missing
        else:
            recipes[rec]['missing'] = missing[:-2]

    return render_template('recipes.html', user=current_user, recipes = recipes, favlist = favlist['fav_list'])

@app.route("/gpt", methods=['GET', 'POST'])
@login_required
def gpt():

    dict_cocktail = {'name': 'Waiting for input...'}

    if request.method == 'POST':
        requested = request.form['text-input']

        gptcocktail = getGPT(username=current_user.username, specialrequest=requested)
        start = gptcocktail.find('{')
        end = gptcocktail.find('}')+1
        if gptcocktail == 'Not enough ingredients':
            dict_cocktail = {'name': 'Too Few Ingredients In Stock', 'description': 'Add more ingredients to your stock, save, and try again'}
        else:
            try:
                dict_cocktail = json.loads(gptcocktail[start:end])
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                dict_cocktail = {'name': 'Bad Generation, Try Again'}
        return render_template('gpt.html', user=current_user, recipe = dict_cocktail)
    
    return render_template('gpt.html', user=current_user, recipe = dict_cocktail)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('index')


## Favorite a recipe [for js function]
@app.route("/fav/<recipe_id>", methods=['POST'])
@login_required
def fav(recipe_id):
    recipeEnt = getRecipe(str(recipe_id))
    favEnt = getFav(current_user.username)

    if not recipeEnt:
        return jsonfiy({'error': 'Post or user favorite list does not exist.'}, 400)
    else:
        favEnt, recipeEnt = addRemoveFav(favEnt, recipeEnt)
    return jsonify({"favs": recipeEnt['favs'], "fav": str(recipe_id) in favEnt['fav_list']})


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