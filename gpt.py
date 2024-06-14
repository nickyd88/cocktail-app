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
        model= 'gpt-3.5-turbo',  #"gpt-3.5-turbo",
        messages=[
            {"role": "system",
            "content": '''
                You are a mixologist at a nice cocktail bar. You are an avid reader of liquor.com and own the savoy cocktail manual and bartenders bible.

                In this conversation, I will provide prompts that are a list of ingredients you must work with, and a list of cocktails that I know I like.
                You will respond with a string that can be converted to a Python dictionary or json in the following format, recommending a new cocktail for me that I may have never seen before.
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
"garnish": "Lime wheel"
}
and
{
"name": "Pisco Sour",
"ratios": [
    "2 oz Pisco",
    "1 oz Lemon Juice",
    "3/4 oz Simple Syrup",
    "1 egg white",
],
"directions": "Dry shake (without ice), then shake with ice and strain into a chilled cocktail glass",
"garnish": "Angostura Bitters"
}
                Include "description": "A brief 1 sentence describing the cocktail and inspiration" and "glass type": "the type of glass that should be used".
                The cocktail should be well balanced. Use famous bartenders like Phil Ward or Joaquin Simo or Anders Erickson for inspiration.
                '''
            },
            {"role": "user", "content": '''
            Suggest a new cocktail for me to make based on my tastes. A list of some of my favorite cocktails are: 
            ''' + ''.join(str(x)+', ' for x in favlist) + '''. The ingredients I have are '''+''.join(str(x)+', ' for x in stocked)+' and egg white. A special request: '+specialrequest
            }
        ]
    )

    return completion.choices[0].message.content

#gptcocktail = getGPT(username='Nick', specialrequest="surprise me")


#print(gptcocktail)

drink = '''{
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
"glass": 'coupe glass'
}'''



testingfunction = '''
client = OpenAI(api_key = getOAIkey())

response = client.images.generate(
    model="dall-e-3",
    prompt='arealistic, simple photo of a single cocktail on a table. No other bottles or glasses or anything else on the the table. just the cocktail. keep in mind the glass parameter from the cocktail, and the name and color of the ingredients: '+drink,
    size='1024x1792',
    quality='standard',
    n=1
)

print(response.data[0].url)
'''


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