import csv
from api_request import *

def avg(caseHashName, csvName):
    if collectionName == 'Spectrum'
    #Collection same: Spectrum or Spectrum 2
    #spectrum price = 0.97
    #SPectrum 2 price = 0.63
    #key price is fixed at 2.50
    #csv should include every data point.
    #csv variabe should be string name of csv, such as for example skins.csv

    sPrice = 97
    s2Price = 0.63
    keyPrice = 250


    with open(csvName, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # retreiving the contents of the CSV file
        totalNumberSkins = 0
        totalPriceSkins = 0
        for lines in csvFile:
            #if not header,
            if lines[1] != 'steam_price':
                #if price was retrived without error (hence e)
                if lines[1] != 'e':
                    totalNumberSkins += 1
                    #prices are in cents, btw
                    totalPriceSkins += int(lines[1])
        print(totalPriceSkins/100)
        print(totalNumberSkins)

        f = requester()
        casePrice = f.get_price_steamAPI(caseHashName)[0]
        casePrice * 100 #casePrice is in dollars, not cents

        openPrice = casePrice + keyPrice
        totalCost = openPrice * totalNumberSkins

        expectedRet = float(totalPriceSkins) / float(totalCost)

    