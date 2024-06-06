from google.cloud import datastore
from flask_login import UserMixin, login_required, login_user, logout_user, current_user

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



ingredients_test = ['Amaro', 'Aperol', 'Campari']

ingredients_family = [
    'Amaro',
    'Aperol',
    'Campari',

    'Sherry',
    'Dry Vermouth',
    'Sweet Vermouth',
    'Lilet Blanc',
    'Apple Brandy',
    'Other Brandy',
    'Cognac',
    'Angostura Bitters',
    'Orange Bitters',
    'Black Walnut Bitters',
    'Chocolate Mole Bitters',
    'Peychaud Bitters',
    'Port',

    'Whiskey',
    'Scotch Whiskey',
    'Bourbon Whiskey',
    'Rye Whiskey',
    'Gin',
    'Vodka',
    'Aged Rum',
    'White Rum',
    'Rhum',

    'Cachasa',
    'Genever',

    'Green Chartreuse',
    'Yellow Chartreuse',
    'Benedictine',
    'Amaretto',
    'Creme de Violette',
    'Creme de Menthe',
    'Creme de Cacao',
    'Creme de Mure',
    'Creme de Cassis',
    'Creme de Peche',

    'Kahlua',
    'Jagermeister',
    'Baileys',

    'Lemon Juice',
    'Lime Juice',
    'Grapefruit Juice',
    'Pineapple Juice',
    'Orange Juice',

    'Simple Syrup',
    'Demarara Syrup',
    'Grenadine',
    'Maple Syrup',
    'Orgeat',
    'Cream of Coconut',

    'Grapes',
    'Blackberries',
    'Peach'
]



def getIngredients():
    return ingredients_test


## Data Store Functions

def getClient():
    return datastore.Client()

def getStock(username):
    client = getClient()
    stock = client.key('stock', username)
    

