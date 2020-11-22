from lxml import html
import json
import requests

page = open('./authors_list.html', "r", encoding='utf-8')
content = page.read()
tree = html.fromstring(content)

authors = tree.xpath('//h2/a/text()')

print(authors)

output = open('data.json', 'w', encoding='utf-8')
json.dump(authors, output)
