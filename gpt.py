from openai import OpenAI
from config import getOAIkey
from database import getFav
from data_functions import getStock
from database import getCocktailsFromDB
from flask import jsonify

def getGPT(username, specialrequest):
    favs = getFav(username)
    stock = getStock(username)
    recipes = getCocktailsFromDB()

    favlist = []
    for fav in favs['fav_list']:
        try:
            favlist.append(recipes[fav]['name'])
        except KeyError:
            pass

    stocked = []
    for item in stock.keys():
        if stock[item]['stocked'] is True:
            stocked.append(item)

    if len(stocked) < 4:
        return 'Not enough ingredients'

    client = OpenAI(api_key = getOAIkey())
    completion = client.chat.completions.create(
        model= 'gpt-4o',  #"gpt-3.5-turbo",
        messages=[
            {"role": "system",
            "content": '''
                You are a mixologist at a nice cocktail bar. You are an avid reader of liquor.com and own the savoy cocktail manual and bartenders bible.

                In this conversation, I will provide prompts that are a list of ingredients you must work with, and a list of cocktails that I know I like.
                You will respond with a string that can be converted to a Python Dictionary in the following format, recommending a new cocktail for me that I may have never seen before.
                Do
                Use this format, here are some examples:

{
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
}

{
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
]
}

                You should also include "description": "A brief 1 sentence describing the cocktail and inspiration" and "glass type": "the type of glass that should be used".
                Only suggest Mezcal at most a quarter of the time unless specifically requested for smoke.
                The cocktail should be well balanced. If serving in a coupe or nick and nora glass, there should be at most 3-4 oz of total wet ingredients.
                '''
            },
            {"role": "user", "content": '''
            Suggest a new cocktail for me to make based on my tastes. A list of some of my favorite cocktails are: 
            ''' + ''.join(str(x)+', ' for x in favlist) + '''. The ingredients I have are '''+''.join(str(x)+', ' for x in stocked)+' special requests: '+specialrequest
            }
        ]
    )

    return completion.choices[0].message.content

#gptcocktail = getGPT(username='Nick', specialrequest="surprise me")


#print(gptcocktail)


old = '''
                You are a mixologist at a nice cocktail bar.
                You are well versed in modern and classic cocktails, and read recipes from places like liquor.com or the savoy cocktail book or the bartenders bible.
                You must respond to recipe requests only in the following format example of JSON:
                    {'name': 'name of cocktail',
                        'ratios': ['1 oz ingredient 1', '1/2 oz ingredient 2', etc],
                        'directions': 'Shake well, double strain into up glass',
                        'garnish': 'Lemon twist',
                        'description': 'a quick 1 or 2 sentence descriptor of the cocktail to entice the consumer.'}.
                Do not include slash n carriage returns in your answer, just a JSON blob.
                You must only use the following ingredients: '''