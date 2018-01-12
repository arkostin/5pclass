#!/usr/bin/python3
from lxml import html
import requests

page = requests.get('http://play.typeracer.com/')
tree = html.fromstring(page.content)
print(tree)
