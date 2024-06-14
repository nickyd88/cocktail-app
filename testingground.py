from gpt import getGPT
import json


user = 'Nick'
instructions = 'Last word inspired, but with scotch, chartreuse and creme de cassis'

#recipe = getGPT(user, instructions).strip()

string = r'{\n"name": "Crimson Rambler",\n"ratios": [\n"1.5 oz Gin",\n"0.75 oz Creme de Cassis",\n"0.5 oz Lemon Juice",\n"1 tsp Grenadine",\n"1 dash Orange Bitters"\n],\n"glass type": "Coupe glass",\n"directions": "Shake all ingredients with ice and strain into a chilled coupe glass.",\n"garnish": "Lemon twist",\n"description": "A floral and fruity cocktail with a deep crimson color, inspired by the vibrant hues of a blooming garden.",\n}'

string = string.replace(r'\n',r'')
string = string.replace(r',}',r'}')

print(string, repr(string))

start = string.find('{')
end = string.find('}')+1

print(string[start:end])

try:
    dict_cocktail = json.loads(string[start:end])
except ValueError:  # includes simplejson.decoder.JSONDecodeError
    dict_cocktail = {'name': 'Bad Generation, Try Again'}

print(dict_cocktail)

