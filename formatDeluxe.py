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
import priceUpdate
from caseCollections import *
import s2finalformat

def FD(case):

    fileUnique = (case) + 'Unique.csv'

    fileEvery = (case) + 'Every.csv'

    #priceFinder
    request = priceFinder.priceRequester

    filePrice = ('P' + fileUnique)

    #
    request.gen_price_csv(request, fileUnique, filePrice)

    everyPrice = ('P' + fileEvery)

    #priceUpdate
    priceUpdate.unique_to_every(filePrice, fileEvery, everyPrice)

    finalname = ((fileUnique[:-10])+ 'final' + '.csv')

    #finalformat
    s2finalformat.finalformat(everyPrice, finalname)

    
