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
import formatDeluxe
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

#def simCase(caseType, amount, fileName, collection = None):

#case = simCase('horizon', 1000000, 'horizon')
# simulate(1000000)
# print('done sim 1')
# danger = simCase('horizon', 1000000, 'danger', "The Danger Zone Collection")
# print('done sim 2')
# chroma = simCase('chroma', 1000000, 'chroma')
# print('done sim 3')
# chroma2 = simCase('chroma', 1000000, 'chroma2', 'The Chroma 2 Collection')
# print('chroma 2')
# chroma3 = simCase('chroma', 1000000, 'chroma3', 'The Chroma 3 Collection')
# print('chroma 3')
# prisma = simCase('prisma', 1000000, 'prisma')
# print('prisma')
# prisma2 = simCase('prisma', 1000000, 'prisma2', 'The Prisma 2 Collection')
# print('prisma2')

#formatDeluxe.FD('danger')

#danger = simCase('horizon', 100, 'dangerTEST', "The Danger Zone Collection")
simulate(100)
# request = requester()
#
# data = request.get_price_steamAPI("Talon Knife | Case Hardened (Field-Tested)")
# print(data)