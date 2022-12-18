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
from simulations import *
import priceFinder
import spectPriceUpdate
from caseCollections import *

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


#simulate(10000)
#request = priceFinder.priceRequester

#request.gen_price_csv(request, 's2unique.csv', 'Ps2unique.csv')
#request.gen_price_csv(request, 'spectunique.csv', 'Pspectunique.csv')
#spectPriceUpdate.unique_to_every('Ps2unique.csv', 's2every.csv', 'Ps2every.csv')
#spectPriceUpdate.unique_to_every('Pspectunique.csv', 'spectevery.csv', 'Pspectevery.csv')

case = simCase('horizon', 1000000, 'horizon')