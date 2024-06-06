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
            'Eammon',
            'Jamie',
            'TEST USER'
            ]


class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username


ingredients_test = ['Amaro', 'Aperol', 'Campari', 'Benedictine']

all_ingredients= [
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
    'Tequila',
    'Mezcal',
    'Absinthe',
    
    'Dry Vermouth',
    'Sweet Vermouth',
    'Aromatized White Wine',
    'Aromatized Red Wine',
    'Sparkling Wine',
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
    'Coffee Liqueur',
    'Rasberry Liqueur',
    'Creme de Cassis',
    'Peach Liqueur',
    'Pimm''s',

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
    'Soda Water',

    'Simple Syrup',
    'Demarara Syrup',
    'Grenadine',
    'Maple Syrup',
    'Honey Syrup',
    'Orgeat',
    'Cream of Coconut',

    'Grapes',
    'Blackberries',
    'Peach',
    'Mint'
]


# Generate list of ingredients
def getIngredients():
    return all_ingredients

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



recipes = {
    'Paper Plane': {
        'ratios': ['3/4 oz Bourbon', '3/4 oz Aperol', '3/4 oz Amaro', '3/4 oz Lemon Juice'],
        'directions': 'Shake vigorously with ice, double strain into up-glass',
        'garnish': 'None',
        'ingredients': ['Bourbon Whiskey', 'Aperol', 'Amaro', 'Lemon Juice']
    },
    'Last Word': {
        'ratios': ['3/4 oz Gin', '3/4 oz Green Chartreuse', '3/4 oz Maraschino Liqueur', '3/4 oz Lime Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lime wheel',
        'ingredients': ['Gin', 'Green Chartreuse', 'Lime Juice', 'Cherry Liqueur']
    },
    'Naked and Famous': {
        'ratios': ['3/4 oz Mezcal', '3/4 oz Aperol', '3/4 oz Yellow Chartreuse', '3/4 oz Lime Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'None',
        'ingredients': ['Mezcal', 'Aperol', 'Yellow Chartreuse', 'Lime Juice']
    },
    'Monte Cassino': {
        'ratios': ['3/4 oz Rye Whiskey', '3/4 oz Benedictine', '3/4 oz Yellow Chartreuse', '3/4 oz Lemon Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Rye Whiskey', 'Benedictine', 'Yellow Chartreuse', 'Lemon Juice']
    },
    'Final Ward': {
        'ratios': ['3/4 oz Rye Whiskey', '3/4 oz Green Chartreuse', '3/4 oz Maraschino Liqueur', '3/4 oz Lemon Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Rye Whiskey', 'Green Chartreuse', 'Lemon Juice', 'Cherry Liqueur']
    },
    'Ward 8': {
        'ratios': ['2 oz Rye Whiskey', '1/2 oz Lemon Juice', '1/2 oz Orange Juice', '1/2 oz Grenadine'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Rye Whiskey', 'Lemon Juice', 'Orange Juice', 'Grenadine']
    },
    'Momisette': {
        'ratios': ['1 1/2 oz Absinthe', '3/4 oz Orgeat', '1/2 oz Lemon Juice', 'Soda Water'],
        'directions': 'Shake Absinthe, simple syrup, lemon juice, and bitters with ice, strain into a highball glass filled with ice, top with soda water',
        'garnish': 'Lemon wheel',
        'ingredients': ['Absinthe', 'Orgeat', 'Lemon Juice', 'Soda Water']
    },
    'Painkiller': {
        'ratios': ['2 oz Aged Rum', '4 oz Pineapple Juice', '1 oz Orange Juice', '1 oz Cream of Coconut'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass filled with ice',
        'garnish': 'Grated nutmeg and pineapple wedge',
        'ingredients': ['Aged Rum', 'Pineapple Juice', 'Orange Juice', 'Cream of Coconut']
    },
    'Pina Colada': {
        'ratios': ['2 oz White Rum', '1 oz Cream of Coconut', '1 oz Pineapple Juice'],
        'directions': 'Blend with ice and strain into a chilled cocktail glass',
        'garnish': 'Pineapple wedge and cherry',
        'ingredients': ['White Rum', 'Cream of Coconut', 'Pineapple Juice']
    },
    'Bee\'s Knees': {
        'ratios': ['2 oz Gin', '3/4 oz Lemon Juice', '3/4 oz Honey Syrup'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Gin', 'Lemon Juice', 'Honey Syrup']
    },
    'White Lady': {
        'ratios': ['2 oz Gin', '3/4 oz Cointreau', '3/4 oz Lemon Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Gin', 'Lemon Juice', 'Orange Liqueur']
    },
    'Pink Lady': {
        'ratios': ['1 1/2 oz Gin', '1/4 oz Applejack', '1/4 oz Lemon Juice', '3/4 oz Grenadine', '1 egg white'],
        'directions': 'Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Gin', 'Apple Brandy', 'Lemon Juice', 'Grenadine']
    },
    'Clover Club': {
        'ratios': ['2 oz Gin', '3/4 oz Lemon Juice', '3/4 oz Raspberry Syrup', '1 egg white'],
        'directions': 'Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Raspberry',
        'ingredients': ['Gin', 'Lemon Juice', 'Raspberry Syrup']
    },
    'Pisco Sour': {
        'ratios': ['2 oz Pisco', '1 oz Lemon Juice', '3/4 oz Simple Syrup', '1 egg white'],
        'directions': 'Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Angostura Bitters',
        'ingredients': ['Pisco', 'Lemon Juice', 'Simple Syrup']
    },
    'Old Fashioned': {
        'ratios': ['2 oz Bourbon or Rye Whiskey', '1/4 oz Demarara Syrup', '2 dashes Angostura Bitters'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Orange twist and cherry',
        'ingredients': ['Bourbon Whiskey', 'Demarara Syrup', 'Angostura Bitters']
    },
    'Oxacan Old Fashioned': {
        'ratios': ['1 1/2 oz Reposado Tequila', '1/2 oz Mezcal', '1/4 oz Simple Syrup', '2 dashes Angostura Bitters or Mole Bitters'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass with a large ice cube',
        'garnish': 'Orange twist',
        'ingredients': ['Tequila', 'Mezcal', 'Angostura Bitters']
    },
    'Enzoni': {
        'ratios': ['1 1/2 oz Gin', '3/4 oz Campari', '1 oz Lemon Juice', '1/2 oz Simple Syrup', '5 grapes'],
        'directions': 'Muddle grapes in a shaker, shake all ingredients with ice and strain into a chilled cocktail glass with fresh ice',
        'garnish': 'Grape',
        'ingredients': ['Gin', 'Campari', 'Lemon Juice', 'Simple Syrup', 'Grapes']
    },
    'Negroni': {
        'ratios': ['1 oz Gin', '1 oz Campari', '1 oz Sweet Vermouth'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass with large ice cube',
        'garnish': 'Orange twist',
        'ingredients': ['Gin', 'Campari', 'Sweet Vermouth']
    },
    'Corpse Reviver #2': {
        'ratios': ['3/4 oz Gin', '3/4 oz Cointreau', '3/4 oz Lillet Blanc', '3/4 oz Lemon Juice', '1 dash Absinthe'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Gin', 'Lemon Juice', 'Absinthe', 'Orange Liqueur', 'Aromatized White Wine']
    }, 
    'Aviation': {
        'ratios': ['2 oz Gin', '1/2 oz Maraschino Liqueur', '1/4 oz Creme de Violette', '3/4 oz Lemon Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Gin', 'Creme de Violette', 'Lemon Juice', 'Cherry Liqueur']
    },
    'Bijou': {
        'ratios': ['1 oz Gin', '1 oz Green Chartreuse', '1 oz Sweet Vermouth'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Gin', 'Green Chartreuse', 'Sweet Vermouth']
    },
    'Blood and Sand': {
        'ratios': ['3/4 oz Scotch Whiskey', '3/4 oz Sweet Vermouth', '3/4 oz Cherry Liqueur', '3/4 oz Orange Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Orange twist',
        'ingredients': ['Scotch Whiskey', 'Sweet Vermouth', 'Orange Juice', 'Cherry Liqueur']
    },
    'Boulevardier': {
        'ratios': ['1 oz Bourbon Whiskey', '1 oz Campari', '1 oz Sweet Vermouth'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Orange twist',
        'ingredients': ['Bourbon Whiskey', 'Campari', 'Sweet Vermouth']
    },
    'Corpse Reviver #1': {
        'ratios': ['1 oz Cognac', '1 oz Calvados', '1/2 oz Sweet Vermouth'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'None',
        'ingredients': ['Cognac', 'Apple Brandy', 'Sweet Vermouth']
    },
    'Daiquiri': {
        'ratios': ['2 oz White Rum', '1 oz Lime Juice', '3/4 oz Simple Syrup'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lime wheel',
        'ingredients': ['White Rum', 'Lime Juice', 'Simple Syrup']
    },
    'Dark and Stormy': {
        'ratios': ['2 oz Spiced Rum', '3 oz Ginger Beer', '1/2 oz Lime Juice'],
        'directions': 'Build in a glass filled with ice',
        'garnish': 'Lime wedge',
        'ingredients': ['Spiced Rum', 'Ginger Beer', 'Lime Juice']
    },
    'French 75': {
        'ratios': ['1 oz Gin', '1/2 oz Lemon Juice', '1/2 oz Simple Syrup', '3 oz Champagne'],
        'directions': 'Shake gin, lemon juice, and simple syrup with ice, strain into a champagne flute, and top with Champagne',
        'garnish': 'Lemon twist',
        'ingredients': ['Gin', 'Lemon Juice', 'Simple Syrup', 'Sparkling Wine']
    },
    'Hemingway Daiquiri': {
        'ratios': ['2 oz White Rum', '1/2 oz Maraschino Liqueur', '3/4 oz Lime Juice', '1/2 oz Grapefruit Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lime wheel',
        'ingredients': ['White Rum', 'Lime Juice', 'Grapefruit Juice', 'Cherry Liqueur']
    },
    'Jack Rose': {
        'ratios': ['2 oz Applejack', '3/4 oz Lemon Juice', '1/2 oz Grenadine'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Apple Brandy', 'Lemon Juice', 'Grenadine']
    },
    'Mai Tai': {
        'ratios': ['1 oz Jamaican Rum', '1 oz Aged Rum', '3/4 oz Lime Juice', '1/2 oz Orange Liqueur', '1/2 oz Orgeat'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Mint sprig',
        'ingredients': ['Jamaican Rum', 'Aged Rum', 'Lime Juice', 'Orange Liqueur', 'Orgeat']
    },
    'Manhattan': {
        'ratios': ['2 oz Rye Whiskey', '1 oz Sweet Vermouth', '2 dashes Angostura Bitters'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Rye Whiskey', 'Sweet Vermouth', 'Angostura Bitters']
    },
    'Martinez': {
        'ratios': ['1 1/2 oz Old Tom Gin', '1 1/2 oz Sweet Vermouth', '1/4 oz Maraschino Liqueur', '1 dash Orange Bitters'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Gin', 'Sweet Vermouth', 'Cherry Liqueur', 'Orange Bitters']
    },
    'Martini': {
        'ratios': ['2 oz Gin', '1 oz Dry Vermouth', '1 dash Orange Bitters, optional'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist or olive',
        'ingredients': ['Gin', 'Dry Vermouth']
    },
    'Margarita': {
        'ratios': ['2 oz Tequila', '1 oz Lime Juice', '3/4 oz Cointreau'],
        'directions': 'Shake with ice and strain into a salt-rimmed glass filled with ice',
        'garnish': 'Lime wedge',
        'ingredients': ['Tequila', 'Lime Juice', 'Orange Liqueur']
    },
    'Mint Julep': {
        'ratios': ['2 oz Bourbon Whiskey', '1/2 oz Simple Syrup', '8-10 Mint Leaves'],
        'directions': 'Muddle mint leaves with simple syrup, fill the glass with crushed ice, add bourbon, and stir',
        'garnish': 'Mint sprig',
        'ingredients': ['Bourbon Whiskey', 'Simple Syrup', 'Mint']
    },
    'Mojito': {
        'ratios': ['2 oz White Rum', '1 oz Lime Juice', '3/4 oz Simple Syrup', '8-10 Mint Leaves', 'Soda Water'],
        'directions': 'Muddle mint leaves with lime juice and simple syrup, add rum and ice, top with soda water',
        'garnish': 'Mint sprig',
        'ingredients': ['White Rum', 'Lime Juice', 'Simple Syrup', 'Mint', 'Soda Water']
    },
    'Moscow Mule': {
        'ratios': ['2 oz Vodka', '1/2 oz Lime Juice', '3 oz Ginger Beer'],
        'directions': 'Build in a copper mug filled with ice, top with ginger beer',
        'garnish': 'Lime wedge',
        'ingredients': ['Vodka', 'Lime Juice', 'Ginger Beer']
    },
    'Jamaican Mule': {
        'ratios': ['2 oz Jamaican Rum', '1/2 oz Lime Juice', '3 oz Ginger Beer'],
        'directions': 'Build in a copper mug filled with ice, top with ginger beer',
        'garnish': 'Lime wedge',
        'ingredients': ['Jamaican Rum', 'Lime Juice', 'Ginger Beer']
    },
    'Kentucky Mule': {
        'ratios': ['2 oz Bourbon', '1/2 oz Lime Juice', '3 oz Ginger Beer'],
        'directions': 'Build in a copper mug filled with ice, top with ginger beer',
        'garnish': 'Lime wedge',
        'ingredients': ['Bourbon Whiskey', 'Lime Juice', 'Ginger Beer']
    },
    'London Mule': {
        'ratios': ['2 oz Gin', '1/2 oz Lime Juice', '3 oz Ginger Beer'],
        'directions': 'Build in a copper mug filled with ice, top with ginger beer',
        'garnish': 'Lime wedge',
        'ingredients': ['Gin', 'Lime Juice', 'Ginger Beer']
    },
    'Paloma': {
        'ratios': ['2 oz Tequila', '1/2 oz Lime Juice', '1/4 oz Simple Syrup', '2 oz Grapefruit Juice', 'Soda Water'],
        'directions': 'Shake all ingredients except soda water, strain into rocks or collins glass with soda water',
        'garnish': 'Lime wedge',
        'ingredients': ['Tequila', 'Lime Juice', 'Simple Syrup', 'Grapefruit Juice', 'Soda Water']
    },
    'Sazerac': {
        'ratios': ['2 oz Rye Whiskey', '1 sugar cube', '2 dashes Peychaud Bitters', 'Absinthe rinse'],
        'directions': 'Muddle sugar with bitters, add whiskey and ice, stir, strain into an absinthe-rinsed glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Rye Whiskey', 'Peychaud Bitters', 'Absinthe']
    },
    'Sidecar': {
        'ratios': ['2 oz Cognac', '3/4 oz Cointreau', '3/4 oz Lemon Juice'],
        'directions': 'Shake with ice and strain into a sugar-rimmed glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Cognac', 'Lemon Juice', 'Orange Liqueur']
    },
    'Singapore Sling': {
        'ratios': ['1 1/2 oz Gin', '1 oz Cherry Heering', '1/2 oz Cointreau', '1/2 oz Benedictine', '4 oz Pineapple Juice', '1/2 oz Lime Juice', '1/4 oz Grenadine', '1 dash Angostura Bitters'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Cherry and pineapple slice',
        'ingredients': ['Gin', 'Cherry Liqueur', 'Benedictine', 'Pineapple Juice', 'Lime Juice', 'Grenadine', 'Angostura Bitters']
    },
    'Southside': {
        'ratios': ['2 oz Gin', '3/4 oz Lime Juice', '3/4 oz Simple Syrup', '8-10 Mint Leaves'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Mint leaf',
        'ingredients': ['Gin', 'Lime Juice', 'Simple Syrup', 'Mint']
    },
    'Tom Collins': {
        'ratios': ['2 oz Gin', '1 oz Lemon Juice', '1/2 oz Simple Syrup', 'Soda Water'],
        'directions': 'Build in a glass filled with ice, top with soda water',
        'garnish': 'Lemon wheel',
        'ingredients': ['Gin', 'Lemon Juice', 'Simple Syrup', 'Soda Water']
    },
    'Whiskey Sour': {
        'ratios': ['2 oz Bourbon Whiskey', '3/4 oz Lemon Juice', '1/2 oz Simple Syrup', '1 Egg White'],
        'directions': 'Dry shake all ingredients, shake with ice, strain into a chilled cocktail glass',
        'garnish': 'Cherry',
        'ingredients': ['Bourbon Whiskey', 'Lemon Juice', 'Simple Syrup']
    },
    'White Russian': {
        'ratios': ['2 oz Vodka', '1 oz Coffee Liqueur', '1 oz Cream'],
        'directions': 'Build in a glass filled with ice, top with cream',
        'garnish': 'None',
        'ingredients': ['Vodka', 'Coffee Liqueur']
    },
    'Vieux Carré': {
        'ratios': ['1 oz Rye Whiskey', '1 oz Cognac', '1 oz Sweet Vermouth', '1/4 oz Benedictine', '2 dashes Peychaud Bitters', '2 dashes Angostura Bitters'],
        'directions': 'Stir with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Rye Whiskey', 'Cognac', 'Sweet Vermouth', 'Benedictine', 'Peychaud Bitters', 'Angostura Bitters']
    },
    'Rum Punch': {
        'ratios': ['1 oz Aged Rum', '1 oz White Rum', '1/2 oz Lime Juice', '1/2 oz Lemon Juice', '1 oz Pineapple Juice', '1 oz Orange Juice', '1/2 oz Grenadine'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Cherry and orange slice',
        'ingredients': ['Aged Rum', 'White Rum', 'Lime Juice', 'Lemon Juice', 'Pineapple Juice', 'Orange Juice', 'Grenadine']
    },
    'French Martini': {
        'ratios': ['2 oz Vodka', '1/2 oz Raspberry Liqueur', '1/2 oz Pineapple Juice'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Vodka', 'Raspberry Liqueur', 'Pineapple Juice']
    },
    'Espresso Martini': {
        'ratios': ['2 oz Vodka', '1/2 oz Coffee Liqueur', '1 oz Fresh Espresso'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': '3 coffee beans',
        'ingredients': ['Vodka', 'Coffee Liqueur']
    },
    'Gold Rush': {
        'ratios': ['2 oz Bourbon Whiskey', '3/4 oz Lemon Juice', '3/4 oz Honey Syrup'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Lemon wheel',
        'ingredients': ['Bourbon Whiskey', 'Lemon Juice', 'Honey Syrup']
    },
    'Pisco Punch': {
        'ratios': ['2 oz Pisco', '1 oz Pineapple Juice', '3/4 oz Lemon Juice', '1/2 oz Simple Syrup'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Pineapple slice',
        'ingredients': ['Pisco', 'Pineapple Juice', 'Lemon Juice', 'Simple Syrup']
    },
    'Brandy Crusta': {
        'ratios': ['2 oz Cognac', '1/2 oz Lemon Juice', '1/2 oz Orange Liqueur', '1/4 oz Maraschino Liqueur', '2 dashes Angostura Bitters'],
        'directions': 'Shake with ice and strain into a sugar-rimmed glass',
        'garnish': 'Lemon twist',
        'ingredients': ['Cognac', 'Lemon Juice', 'Orange Liqueur', 'Cherry Liqueur', 'Angostura Bitters']
    },
    'Jungle Bird': {
        'ratios': ['1 1/2 oz Aged Rum', '3/4 oz Campari', '1/2 oz Lime Juice', '1/2 oz Simple Syrup', '1 1/2 oz Pineapple Juice'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Pineapple slice',
        'ingredients': ['Aged Rum', 'Campari', 'Lime Juice', 'Simple Syrup', 'Pineapple Juice']
    },
    'Penicillin': {
        'ratios': ['2 oz Scotch Whiskey', '3/4 oz Lemon Juice', '3/4 oz Honey-Ginger Syrup', '1/4 oz Islay Scotch Whiskey'],
        'directions': 'Shake with ice and strain into a glass filled with ice, float the Islay Scotch on top',
        'garnish': 'Candied ginger',
        'ingredients': ['Scotch Whiskey', 'Lemon Juice', 'Honey Syrup']
    },
    'Mimosa': {
        'ratios': ['2 oz Orange Juice', '4 oz Champagne'],
        'directions': 'Build in a champagne flute, top with champagne',
        'garnish': 'Orange slice',
        'ingredients': ['Orange Juice']
    },
    'Pegu Club': {
        'ratios': ['2 oz Gin', '3/4 oz Orange Liqueur', '1/2 oz Lime Juice', '1 dash Angostura Bitters', '1 dash Orange Bitters'],
        'directions': 'Shake with ice and strain into a chilled cocktail glass',
        'garnish': 'Lime wheel',
        'ingredients': ['Gin', 'Orange Liqueur', 'Lime Juice', 'Angostura Bitters', 'Orange Bitters']
    },
    'Mai Tai': {
        'ratios': ['1 oz White Rum', '1 oz Aged Rum', '1/2 oz Orange Liqueur', '1/4 oz Orgeat', '3/4 oz Lime Juice'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Mint sprig and lime wheel',
        'ingredients': ['White Rum', 'Aged Rum', 'Orange Liqueur', 'Orgeat', 'Lime Juice']
    },
    'Planter\'s Punch': {
        'ratios': ['1 1/2 oz Aged Rum', '1 oz Orange Juice', '1 oz Pineapple Juice', '1/2 oz Lemon Juice', '1/4 oz Grenadine', '1/4 oz Simple Syrup'],
        'directions': 'Shake with ice and strain into a glass filled with ice',
        'garnish': 'Cherry and orange slice',
        'ingredients': ['Aged Rum', 'Orange Juice', 'Pineapple Juice', 'Lemon Juice', 'Grenadine', 'Simple Syrup']
    }
}

def getCocktails():
    return recipes



