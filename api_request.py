import requests
from settings import keyRet
from time import sleep

#guide to requests:
# payload = {'paint_index': '695', 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now'}
# data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
# dict = data.json()[0]
# print(dict['price'])


class requester:
    def __init__(self):
        #removed api key, as it is not needed (so far).
        pass
    def get_price(self, paint_index, wear):

        wear_info = self.wear_to_name(wear)

        payload = {'paint_index': paint_index, 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now',
                   'min_float': wear_info[1], 'max_float': wear_info[2]
                   }
        data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
        #print(data)


        #catches potential errors, such as impossible floats for skin and bad response from api
        if (data.status_code != 200):
            print('ERROR: request status code not 200')
            return "error: failed status code"
        if (data.status_code == 200 and data.json() == []):
            print("ERROR")
            return "error: skin not found"

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


        return market_name, steam_price, floatdb_price
    
    def wear_to_name(self, wear: float):
        #also returns range
        if 0.00 < wear < 0.07:
            return ['FN', '0.00', '0.07']
        if 0.07 < wear < 0.15:
            return ['MW', '0.07', '0.15']
        if 0.15 < wear < 0.38:
            return ['FT', '0.15', '0.38']
        if 0.38 < wear < 0.45:
            return ['WW', '0.38', '0.45']
        if 0.45 < wear < 1.00:
            return ['BS', '0.45', '1.00']

    def get_collection(self, paint_index):

        payload = {'paint_index': paint_index, 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now',
                   }
        data = requests.get("https://csgofloat.com/api/v1/listings", params=payload)
        # print(data)

        #Error detection
        if (data.status_code != 200):
            print('ERROR: request status code not 200, it is', data.status_code)

            #status code 429 is timeout for too many api calls
            if (data.status_code != 429):
                return "error: failed status code"
            else:
                delay = 120
                sleep(delay)
                return 'retry'

        if (data.status_code == 200 and data.json() == []):
            print("ERROR")
            return "error: skin not found", paint_index

        item = data.json()[0]['item']

        item_name = item['market_hash_name']

        if 'collection' in item:
            collection = item['collection']
        else:
            market_name = item['market_hash_name']
            collection = 'Unknown'
            if 'Knife' in market_name:
                collection = 'Knife'
            if 'Bayonet' in market_name:
                collection = 'Knife'
            if 'Karambit' in market_name:
                collection = 'Knife'
            if 'Daggers' in market_name:
                collection = 'Knife'

            if 'Gloves' in market_name:
                collection = 'Gloves'
            if 'Wraps' in market_name:
                collection = 'Gloves'
        return item_name, collection

# payload = {'paint_index': '259' , 'type': 'buy_now', 'limit': '1'
#                    }
# data = requests.get("https://csgofloat.com/api/v1/listings", params=payload)
#
# for item in data.json():
#     name = item['item']
#     for element in name:
#         print(element + ':')
#         print(name[element])
#
