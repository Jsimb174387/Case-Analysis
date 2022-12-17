import priceFinder
from settings import keyRet
from time import sleep
import csv

def unique_to_every(ufile, efile, newfile):
    with open(ufile, mode='r') as csvfile:
        csvLines = []
        csvfile = csv.reader(csvfile)
        for lines in csvfile:
            csvLines.append(lines)

        price_lines = []
        applines = csvLines[1:]
        for line in applines:
                price_lines.append(line)

    with open(efile, mode='r') as csvfile:
        csvLines = []
        csvfile = csv.reader(csvfile)
        for lines in csvfile:
            csvLines.append(lines)

        name_lines = []
        applines = csvLines[1:]
        for line in applines:
            name_lines.append(line)

    updates_lines = []
    for names in name_lines:
        for prices in price_lines:
            updates_lines.append(prices)

    with open(newfile, mode='w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(
                ['hash_name', 'steam_price', 'floatdb_price'])

            for line in updates_lines:
                filewriter.writerow(line)
        
        
