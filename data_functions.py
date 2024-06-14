from google.cloud import datastore
from flask_login import UserMixin, login_required, login_user, logout_user, current_user
import json
#import jsonify
from database import getUsers, getIngredients, getCocktails
import openai



class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username


## Data Store Functions

def getClient():
    return datastore.Client()



# generate dictionary of ingredients for datastore
def createStockDictionary():
    ingredients = {}
    for i in getIngredients():
        ingredients[i] = {'stocked': False, 'notes': ''}
    return ingredients


def getStock(username):
    # initialize a client
    client = getClient()

    # define the key for the users stock
    stock_key = client.key('stock', username)
    
    #try to retrieve the key
    stock_entity = client.get(stock_key)

    # if exists logic, if not make it
    if stock_entity:
        try:
            stock = entityJson(stock_entity['stock'])
        except KeyError:
            deleteStock(username)
            #create a new entity
            new_entity = datastore.Entity(key=stock_key)
            new_entity.update({
                'username': username,
            })
            new_entity.update({
                'stock': createStockDictionary()
                })
            client.put(new_entity)
            stock = entityJson(new_entity['stock'])
    else:
        #create a new entity
        new_entity = datastore.Entity(key=stock_key)
        new_entity.update({
            'username': username,
        })
        new_entity.update({
            'stock': createStockDictionary()
            })
        client.put(new_entity)
        stock = entityJson(new_entity['stock'])
    
    return updateStockDict(stock, getIngredients())


def updateStockDict(stockdict, allingredients):
    for i in allingredients:
        try:
            stockdict[i]
        except KeyError:
            stockdict[i] = {'stocked': False, 'notes': ''}
    return stockdict


def updateStock(username, stockdict):
    client = getClient()
    key = client.key('stock', username)
    curstock = client.get(key)
    curstock['stock'] = stockdict
    client.put(curstock)


def deleteStock(username):
    client = getClient()
    key = client.key('stock', username)
    client.delete(key)

def entityJson(entity):
    return json.loads(json.dumps(entity, default=lambda o: o.__dict__))




