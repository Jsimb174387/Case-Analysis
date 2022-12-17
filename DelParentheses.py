import json
import csv
from api_request import requester
from keyvalues import KeyValues
import vdf

class slicer:
    
    def __init__(self, ):
        self.file = open("node-csgo-items-parser-master/skins.json")
        
    def write_lines():
        
        csvLines = []
        with open('skins.csv', mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # retreiving the contents of the CSV file
            for lines in csvFile:
                csvLines.append(lines)

        #opens Items_game to look for item_set (which is not the same as collection name, frustratingly enough)
        items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

        #skips header
        app_lines = csvLines[1:]
        update_lines = []
        for line in app_lines:
            #line: ['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear', 'set']
            hname = line[0]
            fparen = hname.rfind("(")
            if fparen != -1:
                line[0] = hname[:fparen]
            update_lines.append(line)

        #overwrites with updated information
        with open('skins.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(
                ['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear', 'sets'])

            for line in update_lines:
                filewriter.writerow(line)

paren = slicer

paren.write_lines()
