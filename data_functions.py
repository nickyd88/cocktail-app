from google.cloud import datastore
from flask_login import UserMixin, login_required, login_user, logout_user, current_user
import json

def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key("visit"))
    entity.update({"timestamp": dt})

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind="visit")
    query.order = ["-timestamp"]

    times = query.fetch(limit=limit)

    return times


def getUsers():
    return ['Nick',
            'Goff',
            'Travis',
            'Eammon'
            ]


class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username



ingredients_test = ['Amaro', 'Aperol', 'Campari', 'Benedictine']

ingredients_family = [
    'Whiskey',
    'Scotch Whiskey',
    'Bourbon Whiskey',
    'Irish Whiskey',
    'Japanese Whiskey',
    'Rye Whiskey',
    'Gin',
    'Vodka',
    'Aged Rum',
    'White Rum',
    'Rhum',
    'Jamaican Rum',
    'Spiced Rum',
    'Absinthe',
    

    'Dry Vermouth',
    'Sweet Vermouth',
    'Aromatized White Wine',
    'Aromatized Red Wine',
    'Apple Brandy',
    'Other Brandy',
    'Cognac',
    'Port',
    'Sherry',


    'Cachasa',
    'Pisco',
    'Genever',
    
    'Amaro',
    'Aperol',
    'Campari',
    'Benedictine',
    'Green Chartreuse',
    'Yellow Chartreuse',

    'Amaretto',
    'Orange Liqueur',
    'Cherry Liqueur',
    'Creme de Violette',
    'Creme de Menthe',
    'Creme de Cassis',
    'Chocolate Liqueur',
    'Rasberry Liqueur',
    'Creme de Cassis',
    'Peach Liqueur',
    'Pimm''s',

    'Kahlua',
    'Jagermeister',
    'Baileys',

    'Angostura Bitters',
    'Orange Bitters',
    'Black Walnut Bitters',
    'Chocolate Mole Bitters',
    'Peychaud Bitters',

    'Lemon Juice',
    'Lime Juice',
    'Grapefruit Juice',
    'Pineapple Juice',
    'Orange Juice',
    'Ginger Beer',

    'Simple Syrup',
    'Demarara Syrup',
    'Grenadine',
    'Maple Syrup',
    'Orgeat',
    'Cream of Coconut',

    'Grapes',
    'Blackberries',
    'Peach',
    'Mint'
]


# Generate list of ingredients
def getIngredients():
    return ingredients_test

# generate dictionary of ingredients for datastore
def createStockDictionary():
    ingredients = {}
    for i in getIngredients():
        ingredients[i] = {'stocked': False, 'notes': ''}
    return ingredients


## Data Store Functions

def getClient():
    return datastore.Client()

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

