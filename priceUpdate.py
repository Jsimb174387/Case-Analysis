import priceFinder
from settings import keyRet
from time import sleep
import csv

def unique_to_every(ufile, efile, newfile):
    with open(ufile, mode='r') as csvfile1:
        #Lines of ufile
        csvLines1 = []
        csvFile = csv.reader(csvfile1)
        for lines in csvFile:
            csvLines1.append(lines)

        price_lines = []
        applines1 = csvLines1[1:]
        for line in applines1:
                price_lines.append(line)

        #price_lines are the lines of the first (unique) file

    with open(efile, mode='r') as csvfile2:
        #Lines of efile
        csvLines2 = []
        csvFile = csv.reader(csvfile2)
        for lines in csvFile:
            csvLines2.append(lines)

        name_lines = []
        applines2 = csvLines2[1:]
        for line in applines2:
            name_lines.append(line)

        #name_lines are the lines of the second (every) file

    updates_lines = []
    for names in name_lines:
        for prices in price_lines:
            if names[0] == prices[0]:
                updates_lines.append(prices)

    with open(newfile, mode='w') as csvfile3:
            filewriter = csv.writer(csvfile3, delimiter=',')
            filewriter.writerow(
                ['hash_name', 'steam_price', 'floatdb_price'])

            for line in updates_lines:
                filewriter.writerow(line)
        
        
