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
from spectrum2 import *
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

#sp = spectrum()
#sp.knife_unbox()
#print(sp.simInventory)

parser = itemParser.skin_parser()

parser.gen_skins_csv()
