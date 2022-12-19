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
import bitskinsAPI

request = requester()

case_data = {
    'chroma' : request.get_price_steamAPI('Chroma Case'),
    'chroma2' : request.get_price_steamAPI('Chroma 2 Case'),
    'chroma3' : request.get_price_steamAPI('Chroma 3 Case'),
    'danger' : request.get_price_steamAPI('Danger Zone Case'),
    'horizon' : request.get_price_steamAPI('Horizon Case'),
    'prisma' : request.get_price_steamAPI('Prisma Case'),
    'prisma2' : request.get_price_steamAPI('Prisma 2 Case'),
    'spect' : request.get_price_steamAPI('Spectrum Case'),
    's2' : request.get_price_steamAPI('Spectrum 2 Case')
    }

print (case_data)

good_case_data = {
    'chroma' : [case_data['chroma'][0].replace('$', ''),
    case_data['chroma'][1].replace('"', '').replace(',', '')],
    
    'chroma2' : [case_data['chroma2'][0].replace('$', ''),
    case_data['chroma2'][1].replace('"', '').replace(',', '')],
    
    'chroma3' : [case_data['chroma3'][0].replace('$', ''),
    case_data['chroma3'][1].replace('"', '').replace(',', '')],
    
    'danger' : [case_data['danger'][0].replace('$', ''),
    case_data['danger'][1].replace('"', '').replace(',', '')],
    
    'horizon' : [case_data['horizon'][0].replace('$', ''),
    case_data['horizon'][1].replace('"', '').replace(',', '')],
    
    'prisma' : [case_data['prisma'][0].replace('$', ''),
    case_data['prisma'][1].replace('"', '').replace(',', '')],
    
    'prisma2' : [case_data['prisma2'][0].replace('$', ''),
    case_data['prisma2'][1].replace('"', '').replace(',', '')],
    
    'spect' : [case_data['spect'][0].replace('$', ''),
    case_data['spect'][1].replace('"', '').replace(',', '')],
    
    's2' : [case_data['s2'][0].replace('$', ''),
    case_data['s2'][1].replace('"', '').replace(',', '')],
    }

print(good_case_data)

def formatSingle(case):
    
    fileUnique = (case) + 'Unique.csv'

    fileEvery = (case) + 'Every.csv'

    priceGuide = []
    with open(fileUnique, mode='r') as csvfile1:
        csvFile1 = csv.reader(csvfile1)
        for lines in csvFile1:
            hashname = lines[0]
            parenpos = (hashname.rfind('('))
            name = hashname[:(parenpos - 1)]
            wear = hashname[(parenpos + 1):-1]
            guide = bitskinsAPI.get_market_info(hashname)
            priceGuide.append([hashname, name, wear, guide[0], guide[1]])

    caseOpens = []
    with open(fileEvery, mode='r') as csvfile2:
        csvFile2 = csv.reader(csvfile2)
        for lines in csvFile2:
            hname = lines[0]
            for element in priceGuide:
                if element[0] == hname:
                    openData = element
            caseOpens.append([case, good_case_data[case][0], good_case_data[case][1], lines[0], openData[1], openData[2], openData[3], openData[4]])

    return caseOpens

def FD(cases):
    
    casesFull = []
    for case in cases:
        casesFull.append(formatSingle(case))

    for num in range(len(cases)):

        with open((cases[num] + 'final.csv'), mode='w') as caseFile:
            filewriter = csv.writer(caseFile, delimiter=',')
            filewriter.writerow(
                ['case_name', 'case_price', 'case_volume', 'hash_name', 'name', 'wear', 'price', 'volume'])

            for line in casesFull[num]:
                filewriter.writerow(line)
    finalDB = []
    
    for x in (range(len(cases))):
        for line in casesFull[x]:
            finalDB.append(line)

    with open('DSFinalDB', mode='w') as finalfile:
        filewriter = csv.writer(finalfile, delimiter=',')
        filewriter.writerow(
            ['case_name', 'case_price', 'case_volume', 'hash_name', 'name', 'wear', 'price', 'volume'])

        for line in finalDB:
            filewriter.writerow(line)
    
"""
    #priceFinder
    request = priceFinder.priceRequester

    #
    request.gen_price_csv(request, fileUnique, filePrice)

    #priceUpdate
    priceUpdate.unique_to_every(filePrice, fileEvery, everyPrice)

    finalname = ((fileUnique[:-10])+ 'final' + '.csv')

    #finalformat
    s2finalformat.finalFormat(everyPrice, finalname)

"""    
