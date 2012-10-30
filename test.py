from brewerydb import *
import json

BreweryDb.configure("")

for beer in json.loads(BreweryDb.search({'type':'beer','q':'unibroue'}))['data']:
    print beer['name']
