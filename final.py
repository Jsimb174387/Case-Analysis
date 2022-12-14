import requests
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
import json
from api_request import requester
import itemParser
from randomCSGO import *
import random
import csv
import vdf

# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.get('https://httpbin.org/get', params=payload)

# api_req = requester()
#
# price = api_req.get_price('1105',0.01)
# print(price)
# collection = api_req.get_collection('1105')
# print(collection)

#r = bernoulli.rvs(0.5, 1)
#print(r)
#
# data = requests.get("https://csgostash.com/skin/1301")
items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

id = '323'
skin = items_game['items_game']["paint_kits"][id]
name = skin['name']

sets = items_game['items_game']['item_sets']
for set in sets:
    for item in sets[set]['items']:
        read = False
        comparitor = ''
        for element in item:
            if element == ']':
                read = False
            if read:
                comparitor = comparitor + element
            if element == '[':
                read = True
        if name == comparitor:
            print(item)