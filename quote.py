import requests
import random
import json

# api url
baseUrl = 'https://goodquotesapi.herokuapp.com/'

# read json authors file
input = open('data.json', 'r', encoding='utf-8')
authors = json.load(input)

# choose author and build url
author = random.choice(authors)
url = baseUrl + 'author/' + author

# fetch data
response = requests.get(url)
data = response.json()

if not data:
    print('Title not found')
    quit()

# choose quote
quoteList = data['quotes']
quote = random.choice(quoteList)


# build signature
signature = '-- ' + quote['author']
if quote['publication'] is not None:
    signature += ', ' + quote['publication']

# print
print('"' + quote['quote'] + '"')
print(signature)
