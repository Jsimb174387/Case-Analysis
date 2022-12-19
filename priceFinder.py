import requests
from settings import keyRet
from time import sleep
import csv
import api_request
import bitskinsAPI

#guide to requests:
# payload = {'paint_index': '695', 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now'}
# data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
# dict = data.json()[0]
# print(dict['price'])


class priceRequester:
    def __init__(self):
        #removed api key, as it is not needed (so far).
        pass
    def get_price(hash_name):

        payload = {'sort_by': 'lowest_price', 'limit': '1',
                   'type': 'buy_now', 'market_hash_name': hash_name
                   }
        data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
        

        #catches potential errors, such as impossible floats for skin and bad response from api
        if (data.status_code != 200):
            print('ERROR: request status code not 200')
            return ["error: failed status code", "error: failed status code"]
        if (data.status_code == 200 and data.json() == []):
            print("ERROR")
            return ["error: skin not found", "error: skin not found"]

        #print(data.json()[0].keys())
        dict = data.json()[0]['item']

        #item keys: dict_keys(['asset_id', 'def_index', 'paint_index', 'paint_seed', 'float_value', 'icon_url',
        # 'd_param', 'is_stattrak', 'is_souvenir', 'rarity', 'quality', 'market_hash_name', 'tradable', 'has_screenshot',
        # 'scm', 'item_name', 'wear_name', 'description', 'collection', 'badges'])

        if 'scm' in dict:
            steam_price = dict['scm']['price']
        else:
            steam_price = 'unknown'
        #always should be able to find market name
        market_name = dict['market_hash_name']

        if 'price' in data.json()[0]:
            floatdb_price = data.json()[0]['price']
        #print(hash_name)
        return steam_price, floatdb_price
    
    def gen_price_csv(self, filename, newfilename):
        csvLines = []
        with open(filename, mode='r') as csvfile:
            csvFile = csv.reader(csvfile)
            for lines in csvFile:
                csvLines.append(lines)
                
            update_lines = []
            for line in csvLines:

                prices = bitskinsAPI.get_market_info(line[0])
                
                update_lines.append([line[0], prices[0], prices[1]])

            csvfile.close()
            
        with open(newfilename, mode='w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(
                ['hash_name', 'steam_price', 'volume'])

            for line in update_lines:
                filewriter.writerow(line)


