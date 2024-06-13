from google.cloud import datastore
import json


def getUsers():
    return ['Nick',
            'Goff',
            'Travis',
            'Eammon',
            'Jamie',
            'Sean M',
            'Highlake',
            'TEST USER'
            ]


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
    'Blanco Tequila',
    'Reposado Tequila',
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
    'Elderflower Liqueur',
    'Rasberry Liqueur',
    'Creme de Cassis',
    'Peach Liqueur',
    'Pimm''s',
    'Suze',
    'Drambuie',

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
    'Espresso',

    'Simple Syrup',
    'Demarara Syrup',
    'Grenadine',
    'Maple Syrup',
    'Honey Syrup',
    'Orgeat',
    'Agave Syrup',
    'Cream of Coconut',
    'Rasberry Syrup',

    'Grapes',
    'Blackberries',
    'Peach',
    'Mint'
]


# Generate list of ingredients
def getIngredients():
    return all_ingredients


## IMPORTANT ## ONLY ADD NEW RECIPES TO THE END OF THIS LIST ## OTHERWISE IDS WILL FAIL
recipes = {
    '1': {
        "name": "Paper Plane",
        "ratios": [
            "3/4 oz Bourbon",
            "3/4 oz Aperol",
            "3/4 oz Amaro",
            "3/4 oz Lemon Juice",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "None",
        "ingredients": ["Bourbon Whiskey", "Aperol", "Amaro", "Lemon Juice"],
        "image": "paper_plane.jpg",
    },
    '2': {
        "name": "Last Word",
        "ratios": [
            "3/4 oz Gin",
            "3/4 oz Green Chartreuse",
            "3/4 oz Maraschino Liqueur",
            "3/4 oz Lime Juice",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "Lime wheel",
        "ingredients": ["Gin", "Green Chartreuse", "Lime Juice", "Cherry Liqueur"],
        "image": "last_word.jpg",
    },
    '3': {
        "name": "Naked and Famous",
        "ratios": [
            "3/4 oz Mezcal",
            "3/4 oz Aperol",
            "3/4 oz Yellow Chartreuse",
            "3/4 oz Lime Juice",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "None",
        "ingredients": ["Mezcal", "Aperol", "Yellow Chartreuse", "Lime Juice"],
        "image": "naked_famous.jpg",
    },
    '4': {
        "name": "Monte Cassino",
        "ratios": [
            "3/4 oz Rye Whiskey",
            "3/4 oz Benedictine",
            "3/4 oz Yellow Chartreuse",
            "3/4 oz Lemon Juice",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "Lemon twist",
        "ingredients": [
            "Rye Whiskey",
            "Benedictine",
            "Yellow Chartreuse",
            "Lemon Juice",
        ],
        "image": "monte_cassino.jpg",
    },
    '5': {
        "name": "Final Ward",
        "ratios": [
            "3/4 oz Rye Whiskey",
            "3/4 oz Green Chartreuse",
            "3/4 oz Maraschino Liqueur",
            "3/4 oz Lemon Juice",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "Lemon twist",
        "ingredients": [
            "Rye Whiskey",
            "Green Chartreuse",
            "Lemon Juice",
            "Cherry Liqueur",
        ],
        "image": "final_ward.jpg",
    },
    '6': {
        "name": "Ward 8",
        "ratios": [
            "2 oz Rye Whiskey",
            "1/2 oz Lemon Juice",
            "1/2 oz Orange Juice",
            "1/2 oz Grenadine",
        ],
        "directions": "Shake with ice and double strain into a chilled up-glass",
        "garnish": "Cherry",
        "ingredients": ["Rye Whiskey", "Lemon Juice", "Orange Juice", "Grenadine"],
        "image": "ward_8.jpg",
    },
    '7': {
        "name": "Momisette",
        "ratios": [
            "1 1/2 oz Absinthe",
            "3/4 oz Orgeat",
            "1/2 oz Lemon Juice",
            "Soda Water",
        ],
        "directions": "Shake Absinthe, simple syrup, lemon juice, and bitters with ice, strain into a highball glass filled with ice, top with soda water",
        "garnish": "Lemon wheel",
        "ingredients": ["Absinthe", "Orgeat", "Lemon Juice", "Soda Water"],
        "image": "momisette.jpg",
    },
    '8': {
        "name": "Painkiller",
        "ratios": [
            "2 oz Aged Rum",
            "4 oz Pineapple Juice",
            "1 oz Orange Juice",
            "1 oz Cream of Coconut",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass filled with ice",
        "garnish": "Grated nutmeg and pineapple wedge",
        "ingredients": [
            "Aged Rum",
            "Pineapple Juice",
            "Orange Juice",
            "Cream of Coconut",
        ],
        "image": "painkiller.jpg",
    },
    '9': {
        "name": "Pina Colada",
        "ratios": ["2 oz White Rum", "1 oz Cream of Coconut", "1 oz Pineapple Juice"],
        "directions": "Blend with ice and strain into a chilled cocktail glass",
        "garnish": "Pineapple wedge and cherry",
        "ingredients": ["White Rum", "Cream of Coconut", "Pineapple Juice"],
        "image": "pina_colada.jpg",
    },
    '10': {
        "name": "Bee's Knees",
        "ratios": ["2 oz Gin", "3/4 oz Lemon Juice", "3/4 oz Honey Syrup"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Lemon Juice", "Honey Syrup"],
        "image": "bees_knees.jpg",
    },
    '11': {
        "name": "White Lady",
        "ratios": ["2 oz Gin", "3/4 oz Cointreau", "3/4 oz Lemon Juice"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Lemon Juice", "Orange Liqueur"],
        "image": "white_lady.jpg",
    },
    '12': {
        "name": "Pink Lady",
        "ratios": [
            "1 1/2 oz Gin",
            "1/4 oz Applejack",
            "1/4 oz Lemon Juice",
            "3/4 oz Grenadine",
            "1 egg white",
        ],
        "directions": "Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass",
        "garnish": "Cherry",
        "ingredients": ["Gin", "Apple Brandy", "Lemon Juice", "Grenadine"],
        "image": "pink_lady.jpg",
    },
    '13': {
        "name": "Clover Club",
        "ratios": [
            "2 oz Gin",
            "3/4 oz Lemon Juice",
            "3/4 oz Raspberry Syrup",
            "1 egg white",
        ],
        "directions": "Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass",
        "garnish": "Raspberry",
        "ingredients": ["Gin", "Lemon Juice", "Raspberry Syrup"],
        "image": "clover_club.jpg",
    },
    '14': {
        "name": "Pisco Sour",
        "ratios": [
            "2 oz Pisco",
            "1 oz Lemon Juice",
            "3/4 oz Simple Syrup",
            "1 egg white",
        ],
        "directions": "Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass",
        "garnish": "Angostura Bitters",
        "ingredients": ["Pisco", "Lemon Juice", "Simple Syrup"],
        "image": "pisco_sour.jpg",
    },
    '15': {
        "name": "Old Fashioned",
        "ratios": [
            "2 oz Bourbon or Rye Whiskey",
            "1/4 oz Demarara Syrup",
            "2 dashes Angostura Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Orange twist and cherry",
        "ingredients": ["Bourbon Whiskey", "Demarara Syrup", "Angostura Bitters"],
        "image": "old_fashioned.jpg",
    },
    '16': {
        "name": "Oaxacan Old Fashioned",
        "ratios": [
            "1 1/2 oz Reposado Tequila",
            "1/2 oz Mezcal",
            "1/4 oz Agave Syrup",
            "2 dashes Angostura Bitters or Mole Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass with a large ice cube",
        "garnish": "Orange twist",
        "ingredients": ["Reposado Tequila", "Mezcal", "Agave Syrup", "Angostura Bitters"],
        "image": "oaxacan.jpg",
    },
    '17': {
        "name": "Maple Old Fashioned",
        "ratios": [
            "2 oz Bourbon",
            "1/4 oz Maple Syrup",
            "2 dashes Angostura Bitters or Black Walnut Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass with a large ice cube",
        "garnish": "Orange twist or cherry",
        "ingredients": ["Bourbon Whiskey", "Maple Syrup", "Angostura Bitters"],
        "image": "maple_fashioned.jpg",
    },
    '18': {
        "name": "Enzoni",
        "ratios": [
            "1 1/2 oz Gin",
            "3/4 oz Campari",
            "1 oz Lemon Juice",
            "1/2 oz Simple Syrup",
            "5 grapes (red or green)",
        ],
        "directions": "Muddle grapes in a shaker, shake all ingredients with ice and strain into a chilled cocktail glass with fresh ice",
        "garnish": "Grape",
        "ingredients": ["Gin", "Campari", "Lemon Juice", "Simple Syrup", "Grapes"],
        "image": "enzoni.jpg",
    },
    '19': {
        "name": "Negroni",
        "ratios": ["1 oz Gin", "1 oz Campari", "1 oz Sweet Vermouth"],
        "directions": "Stir with ice and strain into a chilled cocktail glass with large ice cube",
        "garnish": "Orange twist",
        "ingredients": ["Gin", "Campari", "Sweet Vermouth"],
        "image": "negroni.jpg",
    },
    '20': {
        "name": "Corpse Reviver #2",
        "ratios": [
            "3/4 oz Gin",
            "3/4 oz Cointreau",
            "3/4 oz Lillet Blanc",
            "3/4 oz Lemon Juice",
            "1 dash Absinthe",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": [
            "Gin",
            "Lemon Juice",
            "Absinthe",
            "Orange Liqueur",
            "Aromatized White Wine",
        ],
        "image": "corpse_reviver_2.jpg",
    },
    '21': {
        "name": "Aviation",
        "ratios": [
            "2 oz Gin",
            "1/2 oz Maraschino Liqueur",
            "1/4 oz Creme de Violette",
            "3/4 oz Lemon Juice",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Cherry",
        "ingredients": ["Gin", "Creme de Violette", "Lemon Juice", "Cherry Liqueur"],
        "image": "aviation.png",
    },
    '22': {
        "name": "Bijou",
        "ratios": ["1 oz Gin", "1 oz Green Chartreuse", "1 oz Sweet Vermouth"],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Green Chartreuse", "Sweet Vermouth"],
        "image": "default.jpg",
    },
    '23': {
        "name": "Blood and Sand",
        "ratios": [
            "3/4 oz Scotch Whiskey",
            "3/4 oz Sweet Vermouth",
            "3/4 oz Cherry Liqueur",
            "3/4 oz Orange Juice",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Orange twist",
        "ingredients": [
            "Scotch Whiskey",
            "Sweet Vermouth",
            "Orange Juice",
            "Cherry Liqueur",
        ],
        "image": "default.jpg",
    },
    '24': {
        "name": "Boulevardier",
        "ratios": ["1 oz Bourbon Whiskey", "1 oz Campari", "1 oz Sweet Vermouth"],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Orange twist",
        "ingredients": ["Bourbon Whiskey", "Campari", "Sweet Vermouth"],
        "image": "boulevardier.jpg",
    },
    '25': {
        "name": "Corpse Reviver #1",
        "ratios": ["1 oz Cognac", "1 oz Calvados", "1/2 oz Sweet Vermouth"],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "None",
        "ingredients": ["Cognac", "Apple Brandy", "Sweet Vermouth"],
        "image": "default.jpg",
    },
    '26': {
        "name": "Daiquiri",
        "ratios": ["2 oz White Rum", "1 oz Lime Juice", "3/4 oz Simple Syrup"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lime wheel",
        "ingredients": ["White Rum", "Lime Juice", "Simple Syrup"],
        "image": "daiquiri.jpg",
    },
    '27': {
        "name": "Dark and Stormy",
        "ratios": ["2 oz Spiced Rum", "3 oz Ginger Beer", "1/2 oz Lime Juice"],
        "directions": "Build in a glass filled with ice",
        "garnish": "Lime wedge",
        "ingredients": ["Spiced Rum", "Ginger Beer", "Lime Juice"],
        "image": "default.jpg",
    },
    '28': {
        "name": "French 75",
        "ratios": [
            "1 oz Gin",
            "1/2 oz Lemon Juice",
            "1/2 oz Simple Syrup",
            "3 oz Champagne",
        ],
        "directions": "Shake gin, lemon juice, and simple syrup with ice, strain into a champagne flute, and top with Champagne",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Lemon Juice", "Simple Syrup", "Sparkling Wine"],
        "image": "french_75.jpg",
    },
    '29': {
        "name": "Hemingway Daiquiri",
        "ratios": [
            "2 oz White Rum",
            "1/2 oz Maraschino Liqueur",
            "3/4 oz Lime Juice",
            "1/2 oz Grapefruit Juice",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lime wheel",
        "ingredients": [
            "White Rum",
            "Lime Juice",
            "Grapefruit Juice",
            "Cherry Liqueur",
        ],
        "image": "default.jpg",
    },
    '30': {
        "name": "Sidecar",
        "ratios": ["2 oz Cognac", "3/4 oz Cointreau", "3/4 oz Lemon Juice"],
        "directions": "Shake with ice and strain into a sugar-rimmed glass",
        "garnish": "Lemon twist",
        "ingredients": ["Cognac", "Lemon Juice", "Orange Liqueur"],
        "image": "sidecar.jpg",
    },
    '31': {
        "name": "Jack Rose",
        "ratios": ["2 oz Applejack", "3/4 oz Lemon Juice", "1/2 oz Grenadine"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Cherry",
        "ingredients": ["Apple Brandy", "Lemon Juice", "Grenadine"],
        "image": "default.jpg",
    },
    '32': {
        "name": "Mai Tai",
        "ratios": [
            "1 oz White Rum",
            "1 oz Aged Rum",
            "1/2 oz Orange Liqueur",
            "1/4 oz Orgeat",
            "3/4 oz Lime Juice",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Mint sprig and lime wheel",
        "ingredients": [
            "White Rum",
            "Aged Rum",
            "Orange Liqueur",
            "Orgeat",
            "Lime Juice",
        ],
        "image": "mai_tai.jpg",
    },
    '33': {
        "name": "Manhattan",
        "ratios": [
            "2 oz Rye Whiskey",
            "1 oz Sweet Vermouth",
            "2 dashes Angostura Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Cherry",
        "ingredients": ["Rye Whiskey", "Sweet Vermouth", "Angostura Bitters"],
        "image": "manhattan.jpg",
    },
    '34': {
        "name": "Vieux Carré",
        "ratios": [
            "1 oz Rye Whiskey",
            "1 oz Cognac",
            "1 oz Sweet Vermouth",
            "1/4 oz Benedictine",
            "2 dashes Peychaud Bitters",
            "2 dashes Angostura Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": [
            "Rye Whiskey",
            "Cognac",
            "Sweet Vermouth",
            "Benedictine",
            "Peychaud Bitters",
            "Angostura Bitters",
        ],
        "image": "vieux_carre.jpg",
    },
    '35': {
        "name": "Martinez",
        "ratios": [
            "1 1/2 oz Old Tom Gin",
            "1 1/2 oz Sweet Vermouth",
            "1/4 oz Maraschino Liqueur",
            "1 dash Orange Bitters",
        ],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Sweet Vermouth", "Cherry Liqueur", "Orange Bitters"],
        "image": "default.jpg",
    },
    '36': {
        "name": "Martini",
        "ratios": ["2 oz Gin", "1 oz Dry Vermouth", "1 dash Orange Bitters, optional"],
        "directions": "Stir with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist or olive",
        "ingredients": ["Gin", "Dry Vermouth"],
        "image": "default.jpg",
    },
    '37': {
        "name": "Margarita",
        "ratios": ["2 oz Blanco Tequila", "1 oz Lime Juice", "3/4 oz Cointreau"],
        "directions": "Shake with ice and strain into a salt-rimmed glass filled with ice",
        "garnish": "Lime wedge",
        "ingredients": ["Blanco Tequila", "Lime Juice", "Orange Liqueur"],
        "image": "default.jpg",
    },
    '38': {
        "name": "Mint Julep",
        "ratios": ["2 oz Bourbon Whiskey", "1/2 oz Simple Syrup", "8-10 Mint Leaves"],
        "directions": "Muddle mint leaves with simple syrup, fill the glass with crushed ice, add bourbon, and stir",
        "garnish": "Mint sprig",
        "ingredients": ["Bourbon Whiskey", "Simple Syrup", "Mint"],
        "image": "default.jpg",
    },
    '39': {
        "name": "Mojito",
        "ratios": [
            "2 oz White Rum",
            "1 oz Lime Juice",
            "3/4 oz Simple Syrup",
            "8-10 Mint Leaves",
            "Soda Water",
        ],
        "directions": "Muddle mint leaves with lime juice and simple syrup, add rum and ice, top with soda water",
        "garnish": "Mint sprig",
        "ingredients": [
            "White Rum",
            "Lime Juice",
            "Simple Syrup",
            "Mint",
            "Soda Water",
        ],
        "image": "default.jpg",
    },
    '40': {
        "name": "Moscow Mule",
        "ratios": ["2 oz Vodka", "1/2 oz Lime Juice", "3 oz Ginger Beer"],
        "directions": "Build in a copper mug filled with ice, top with ginger beer",
        "garnish": "Lime wedge",
        "ingredients": ["Vodka", "Lime Juice", "Ginger Beer"],
        "image": "default.jpg",
    },
    '41': {
        "name": "Jamaican Mule",
        "ratios": ["2 oz Jamaican Rum", "1/2 oz Lime Juice", "3 oz Ginger Beer"],
        "directions": "Build in a copper mug filled with ice, top with ginger beer",
        "garnish": "Lime wedge",
        "ingredients": ["Jamaican Rum", "Lime Juice", "Ginger Beer"],
        "image": "default.jpg",
    },
    '42': {
        "name": "Kentucky Mule",
        "ratios": ["2 oz Bourbon", "1/2 oz Lime Juice", "3 oz Ginger Beer"],
        "directions": "Build in a copper mug filled with ice, top with ginger beer",
        "garnish": "Lime wedge",
        "ingredients": ["Bourbon Whiskey", "Lime Juice", "Ginger Beer"],
        "image": "default.jpg",
    },
    '43': {
        "name": "London Mule",
        "ratios": ["2 oz Gin", "1/2 oz Lime Juice", "3 oz Ginger Beer"],
        "directions": "Build in a copper mug filled with ice, top with ginger beer",
        "garnish": "Lime wedge",
        "ingredients": ["Gin", "Lime Juice", "Ginger Beer"],
        "image": "default.jpg",
    },
    '44': {
        "name": "Paloma",
        "ratios": [
            "2 oz Blanco Tequila",
            "1/2 oz Lime Juice",
            "1/4 oz Simple Syrup",
            "2 oz Grapefruit Juice",
            "Soda Water",
        ],
        "directions": "Shake all ingredients except soda water, strain into rocks or collins glass with soda water",
        "garnish": "Lime wedge",
        "ingredients": [
            "Blanco Tequila",
            "Lime Juice",
            "Simple Syrup",
            "Grapefruit Juice",
            "Soda Water",
        ],
        "image": "default.jpg",
    },
    '45': {
        "name": "Sazerac",
        "ratios": [
            "2 oz Rye Whiskey",
            "1 sugar cube",
            "2 dashes Peychaud Bitters",
            "Absinthe rinse",
        ],
        "directions": "Muddle sugar with bitters, add whiskey and ice, stir, strain into an absinthe-rinsed glass without ice",
        "garnish": "Lemon twist",
        "ingredients": ["Rye Whiskey", "Peychaud Bitters", "Absinthe"],
        "image": "sazerac.jpg",
    },
    '46': {
        "name": "Amaretto Sour",
        "ratios": [
            "1.5 oz Amaretto",
            "3/4 oz Apple Brandy",
            "1 oz Lemon Juice",
            "1/4 oz Simple Syrup",
            "Egg white",
        ],
        "directions": "Dry shake, then add ice and shake well. Strain into rocks glass with ice",
        "garnish": "Lemon twist or cocktail cherry",
        "ingredients": ["Amaretto", "Apple Brandy", "Lemon Juice", "Simple Syrup"],
        "image": "amaretto_sour.jpg",
    },   
    '47': {
        "name": "Singapore Sling",
        "ratios": [
            "1 1/2 oz Gin",
            "1 oz Cherry Heering",
            "1/2 oz Cointreau",
            "1/2 oz Benedictine",
            "4 oz Pineapple Juice",
            "1/2 oz Lime Juice",
            "1/4 oz Grenadine",
            "1 dash Angostura Bitters",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Cherry and pineapple slice",
        "ingredients": [
            "Gin",
            "Cherry Liqueur",
            "Benedictine",
            "Pineapple Juice",
            "Lime Juice",
            "Grenadine",
            "Angostura Bitters",
        ],
        "image": "default.jpg",
    },
    '48': {
        "name": "Southside",
        "ratios": [
            "2 oz Gin",
            "3/4 oz Lime Juice",
            "3/4 oz Simple Syrup",
            "8-10 Mint Leaves",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Mint leaf",
        "ingredients": ["Gin", "Lime Juice", "Simple Syrup", "Mint"],
        "image": "default.jpg",
    },
    '49': {
        "name": "Tom Collins",
        "ratios": ["2 oz Gin", "1 oz Lemon Juice", "1/2 oz Simple Syrup", "Soda Water"],
        "directions": "Build in a glass filled with ice, top with soda water",
        "garnish": "Lemon wheel",
        "ingredients": ["Gin", "Lemon Juice", "Simple Syrup", "Soda Water"],
        "image": "default.jpg",
    },
    '50': {
        "name": "Whiskey Sour",
        "ratios": [
            "2 oz Bourbon Whiskey",
            "3/4 oz Lemon Juice",
            "1/2 oz Simple Syrup",
            "1 Egg White",
        ],
        "directions": "Dry shake all ingredients, shake with ice, strain into a chilled cocktail glass",
        "garnish": "Cherry",
        "ingredients": ["Bourbon Whiskey", "Lemon Juice", "Simple Syrup"],
        "image": "default.jpg",
    },
    '51': {
        "name": "White Russian",
        "ratios": ["2 oz Vodka", "1 oz Coffee Liqueur", "1 oz Cream"],
        "directions": "Build in a glass filled with ice, top with cream",
        "garnish": "None",
        "ingredients": ["Vodka", "Coffee Liqueur"],
        "image": "default.jpg",
    },
    '52': {
        "name": "Rum Punch",
        "ratios": [
            "1 oz Aged Rum",
            "1 oz White Rum",
            "1/2 oz Lime Juice",
            "1/2 oz Lemon Juice",
            "1 oz Pineapple Juice",
            "1 oz Orange Juice",
            "1/2 oz Grenadine",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Cherry and orange slice",
        "ingredients": [
            "Aged Rum",
            "White Rum",
            "Lime Juice",
            "Lemon Juice",
            "Pineapple Juice",
            "Orange Juice",
            "Grenadine",
        ],
        "image": "default.jpg",
    },
    '53': {
        "name": "French Martini",
        "ratios": ["2 oz Vodka", "1/2 oz Raspberry Liqueur", "1/2 oz Pineapple Juice"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lemon twist",
        "ingredients": ["Vodka", "Raspberry Liqueur", "Pineapple Juice"],
        "image": "default.jpg",
    },
    '54': {
        "name": "Espresso Martini",
        "ratios": ["2 oz Vodka", "1/2 oz Coffee Liqueur", "1 oz Fresh Espresso"],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "3 coffee beans",
        "ingredients": ["Vodka", "Coffee Liqueur", "Espresso"],
        "image": "default.jpg",
    },
    '55': {
        "name": "Gold Rush",
        "ratios": ["2 oz Bourbon Whiskey", "3/4 oz Lemon Juice", "3/4 oz Honey Syrup"],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Lemon wheel",
        "ingredients": ["Bourbon Whiskey", "Lemon Juice", "Honey Syrup"],
        "image": "default.jpg",
    },
    '56': {
        "name": "Pisco Punch",
        "ratios": [
            "2 oz Pisco",
            "1 oz Pineapple Juice",
            "3/4 oz Lemon Juice",
            "1/2 oz Simple Syrup",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Pineapple slice",
        "ingredients": ["Pisco", "Pineapple Juice", "Lemon Juice", "Simple Syrup"],
        "image": "default.jpg",
    },
    '57': {
        "name": "Brandy Crusta",
        "ratios": [
            "2 oz Cognac",
            "1/2 oz Lemon Juice",
            "1/2 oz Orange Liqueur",
            "1/4 oz Maraschino Liqueur",
            "2 dashes Angostura Bitters",
        ],
        "directions": "Shake with ice and strain into a sugar-rimmed glass",
        "garnish": "Lemon twist",
        "ingredients": [
            "Cognac",
            "Lemon Juice",
            "Orange Liqueur",
            "Cherry Liqueur",
            "Angostura Bitters",
        ],
        "image": "default.jpg",
    },
    '58': {
        "name": "Jungle Bird",
        "ratios": [
            "1 1/2 oz Aged Rum",
            "3/4 oz Campari",
            "1/2 oz Lime Juice",
            "1/2 oz Simple Syrup",
            "1 1/2 oz Pineapple Juice",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Pineapple slice",
        "ingredients": [
            "Aged Rum",
            "Campari",
            "Lime Juice",
            "Simple Syrup",
            "Pineapple Juice",
        ],
        "image": "default.jpg",
    },
    '59': {
        "name": "Penicillin",
        "ratios": [
            "2 oz Scotch Whiskey",
            "3/4 oz Lemon Juice",
            "3/4 oz Honey-Ginger Syrup",
            "1/4 oz Islay Scotch Whiskey",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice, float the Islay Scotch on top",
        "garnish": "Candied ginger",
        "ingredients": ["Scotch Whiskey", "Lemon Juice", "Honey Syrup"],
        "image": "default.jpg",
    },
    '60': {
        "name": "Mimosa",
        "ratios": ["2 oz Orange Juice", "4 oz Champagne"],
        "directions": "Build in a champagne flute, top with champagne",
        "garnish": "Orange slice",
        "ingredients": ["Orange Juice", "Sparkling Wine"],
        "image": "default.jpg",
    },
    '61': {
        "name": "Pegu Club",
        "ratios": [
            "2 oz Gin",
            "3/4 oz Orange Liqueur",
            "1/2 oz Lime Juice",
            "1 dash Angostura Bitters",
            "1 dash Orange Bitters",
        ],
        "directions": "Shake with ice and strain into a chilled cocktail glass",
        "garnish": "Lime wheel",
        "ingredients": [
            "Gin",
            "Orange Liqueur",
            "Lime Juice",
            "Angostura Bitters",
            "Orange Bitters",
        ],
        "image": "default.jpg",
    },
    '62': {
        "name": "Planter's Punch",
        "ratios": [
            "1 1/2 oz Aged Rum",
            "1 oz Orange Juice",
            "1 oz Pineapple Juice",
            "1/2 oz Lemon Juice",
            "1/4 oz Grenadine",
            "1/4 oz Simple Syrup",
        ],
        "directions": "Shake with ice and strain into a glass filled with ice",
        "garnish": "Cherry and orange slice",
        "ingredients": [
            "Aged Rum",
            "Orange Juice",
            "Pineapple Juice",
            "Lemon Juice",
            "Grenadine",
            "Simple Syrup",
        ],
        "image": "default.jpg",
    },
    '63': {
        "name": "Blackberry Fencehopper",
        "ratios": [
            "2 oz Gin",
            "1 oz Lemon Juice",
            "1/2 oz Simple Syrup",
            "5-6 Blackberries",
        ],
        "directions": "Muddle blackberries with simple syrup in a shaker. Add gin and lemon juice, shake with ice, strain into a glass filled with ice.",
        "garnish": "Blackberry and lemon wheel",
        "ingredients": ["Gin", "Lemon Juice", "Simple Syrup", "Blackberries"],
        "image": "default.jpg",
    },
    '64': {
        "name": "Maple Peach Smash",
        "ratios": [
            "2 oz Bourbon",
            "1/2 oz Maple Syrup",
            "1/2 Peach (skinned)",
            "1/2 oz Lemon Juice",
            "Soda Water",
        ],
        "directions": "Muddle peach slices in a shaker. Add bourbon, maple syrup, and lemon juice. Shake with ice, strain into a glass with ice, top with seltzer",
        "garnish": "Peach slice",
        "ingredients": [
            "Bourbon Whiskey",
            "Maple Syrup",
            "Lemon Juice",
            "Peach",
            "Soda Water",
        ],
        "image": "default.jpg",
    },
    '65': {
        "name": "Chocolate Espresso Martini",
        "ratios": [
            "1 oz Vodka",
            "1 oz Coffee Liqueur",
            "1 oz Espresso",
            "1/2 oz Chocolate Liqueur",
        ],
        "directions": "Shake all ingredients with ice and strain into a chilled martini glass.",
        "garnish": "Coffee beans",
        "ingredients": ["Vodka", "Coffee Liqueur", "Espresso", "Chocolate Liqueur"],
        "image": "default.jpg",
    },
    '66': {
        "name": "Revolver",
        "ratios": ["2 oz Bourbon", "1/2 oz Coffee Liqueur", "2 dashes Orange Bitters"],
        "directions": "Stir all ingredients with ice and strain into a chilled glass.",
        "garnish": "Orange twist",
        "ingredients": ["Bourbon Whiskey", "Coffee Liqueur", "Orange Bitters"],
        "image": "default.jpg",
    },
    '67': {
        "name": "Between the Sheets",
        "ratios": [
            "1 oz Brandy",
            "1 oz Light Rum",
            "1 oz Triple Sec",
            "1/2 oz Lemon Juice",
        ],
        "directions": "Shake all ingredients with ice and strain into a chilled glass.",
        "garnish": "Lemon twist",
        "ingredients": ["Other Brandy", "White Rum", "Orange Liqueur", "Lemon Juice"],
        "image": "default.jpg",
    },
    '68': {
        "name": "Embassy",
        "ratios": [
            "1 oz Brandy",
            "1 oz Jamaican Rum",
            "1/2 oz Cointreau",
            "1/2 oz Lime Juice",
            "1 dash Angostura Bitters",
        ],
        "directions": "Shake all ingredients with ice and strain into a chilled glass.",
        "garnish": "Lime twist",
        "ingredients": [
            "Other Brandy",
            "Jamaican Rum",
            "Orange Liqueur",
            "Lime Juice",
            "Angostura Bitters",
        ],
        "image": "default.jpg",
    },
    '69': {
        "name": "Americano",
        "ratios": ["1 oz Campari", "1 oz Sweet Vermouth", "Splash of Soda Water"],
        "directions": "Build in a glass with ice and top with soda water.",
        "garnish": "Orange slice",
        "ingredients": ["Campari", "Sweet Vermouth"],
        "image": "default.jpg",
    },
    '70': {
        "name": "White Negroni",
        "ratios": ["1 oz Gin", "1 oz Lillet Blanc", "3/4 oz Suze"],
        "directions": "Stir all ingredients with ice and strain into a chilled glass.",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Aromatized White Wine", "Suze"],
        "image": "white_negroni.jpg",
    },
    '71': {
        "name": "Elder Fashion Royale",
        "ratios": [
            "2 oz Gin",
            "1/2 oz Elderflower Liqueur",
            "1 dash Angostura Bitters",
        ],
        "directions": "Stir all ingredients with ice and strain into a glass.",
        "garnish": "Lemon twist",
        "ingredients": ["Gin", "Elderflower Liqueur", "Angostura Bitters"],
        "image": "default.jpg",
    },
    '72': {
        "name": "Kir",
        "ratios": ["1/2 oz Crème de Cassis", "5 oz Dry White Wine"],
        "directions": "Pour crème de cassis into a wine glass and top with white wine.",
        "garnish": "None",
        "ingredients": ["Creme de Cassis", "White Wine"],
        "image": "default.jpg",
    },
    '73': {
        "name": "Kir Royale",
        "ratios": ["1/2 oz Crème de Cassis", "5 oz Champagne"],
        "directions": "Pour crème de cassis into a champagne flute and top with champagne.",
        "garnish": "None",
        "ingredients": ["Creme de Cassis", "Sparkling Wine"],
        "image": "default.jpg",
    },
    '74': {
        "name": "The Conference",
        "ratios": [
            "1/2 oz Rye Whiskey",
            "1/2 oz Bourbon Whiskey",
            "1/2 oz Apple Brandy",
            "1/2 oz Cognac",
            "1 Barspoon Demarara Syrup",
            "2 dashes Angostura Bitters",
            "1 dash chocolate mole bitters",
        ],
        "directions": "Stir over ice, double strain into rocks glass with large ice.",
        "garnish": "Lemon and Orange twist",
        "ingredients": [
            "Rye Whiskey",
            "Bourbon Whiskey",
            "Apple Brandy",
            "Cognac",
            "Demarara Syrup",
            "Angostura Bitters",
            "Chocolate Mole Bitters",
        ],
        "image": "conference.jpg",
    },
}


def getCocktails():
    return recipes


def addDefaultImages():
    clist = getCocktails()
    for item in clist.keys():
        try:
            clist[item]['image']
        except KeyError:
            clist[item]['image'] = 'default.jpg'
    print(clist)

#addDefaultImages()



def initCocktailsDB():
    # This will ovewrite only entries that don't exist or are different.
    client = datastore.Client()
    all_recipes = getCocktails()

    for recipeid in all_recipes.keys():
        recipe_key = client.key('recipe', recipeid) # recipe table, recipe id.
        recipe_entity = client.get(recipe_key)

        if recipe_entity:
            # update basic recipe info. excludes name, id, favs
            recipe_entity['ratios'] = all_recipes[recipeid]['ratios']
            recipe_entity['directions'] = all_recipes[recipeid]['directions']
            recipe_entity['garnish'] = all_recipes[recipeid]['garnish']
            recipe_entity['ingredients'] = all_recipes[recipeid]['ingredients']
            recipe_entity['image'] = all_recipes[recipeid]['image']
            client.put(recipe_entity)
        else:
            # create new entity for recipe
            new_recipe = datastore.Entity(key=recipe_key)
            new_recipe.update({
                'name': all_recipes[recipeid]['name'],
                'ratios': all_recipes[recipeid]['ratios'],
                'directions': all_recipes[recipeid]['directions'],
                'garnish': all_recipes[recipeid]['garnish'],
                'ingredients': all_recipes[recipeid]['ingredients'],
                'image': all_recipes[recipeid]['image'],
                'favs': '0'
            })
            client.put(new_recipe)


def getCocktailsFromDB():
    client = datastore.Client()
    query = client.query(kind='recipe')
    results = list(query.fetch())
    dictionary = {x.key.id_or_name: x for x in results}
    return dictionary


def initFavsDB():
    # This will only add new users with an empty list.
    client = datastore.Client()
    users = getUsers()

    for user in users:
        user_key = client.key('favs', user) # favs table, user as the key id.
        user_entity = client.get(user_key)
        if user_entity:
            # ignore, continue
            pass
        else:
            # create new user fav list
            new_user = datastore.Entity(key=user_key)
            new_user.update({
                'fav_list': []
            })
            client.put(new_user)

def getFavsDB():
    client = datastore.Client()
    query = client.query(kind='favs')
    results = list(query.fetch())
    dictionary = {x.key.id_or_name: x for x in results}
    return dictionary


def getRecipe(id):
    client = datastore.Client()
    recipe_key = client.key('recipe', id) # recipe table, recipe id.
    recipe_entity = client.get(recipe_key)
    return recipe_entity


def getFav(userid):
    client = datastore.Client()
    fav_key = client.key('favs', userid) # recipe table, recipe id.
    fav_entity = client.get(fav_key)
    if fav_entity:
        # return fav list
        return fav_entity
    else:
        # create new user fav list
        new_user = datastore.Entity(key=fav_key)
        new_user.update({
            'fav_list': []
        })
        client.put(new_user)
        return new_user

def addRemoveFav(fav_entity, recipe_entity):
    client = datastore.Client()
    if recipe_entity.key.id_or_name in fav_entity['fav_list']:
        fav_entity['fav_list'].remove(str(recipe_entity.key.id_or_name))
        recipe_entity['favs'] = str(int(recipe_entity['favs']) - 1)
    else:
        fav_entity['fav_list'].append(str(recipe_entity.key.id_or_name))
        recipe_entity['favs'] = str(int(recipe_entity['favs']) + 1)

    client.put(fav_entity)
    client.put(recipe_entity)
    return fav_entity, recipe_entity
    





#### INITIALIZATION ####

#initCocktailsDB()
#initFavsDB()


#print(recipes)
#print(recipesDB[1].key.id_or_name)

