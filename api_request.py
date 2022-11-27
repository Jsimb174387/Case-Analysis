import requests
from settings import keyRet


#guide to requests:
# payload = {'paint_index': '695', 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now'}
# data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
# dict = data.json()[0]
# print(dict['price'])


class requester:
    def __init__(self):
        pass
    def getPrice(self, paint_index, wear):

        wear_info = self.wear_to_name(wear)

        payload = {'paint_index': '695', 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now',
                   'min_float': wear_info[1], 'max_float': wear_info[2]
                   }
        data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
        dict = data.json()[0]['item']

        #item keys: dict_keys(['asset_id', 'def_index', 'paint_index', 'paint_seed', 'float_value', 'icon_url',
        # 'd_param', 'is_stattrak', 'is_souvenir', 'rarity', 'quality', 'market_hash_name', 'tradable', 'has_screenshot',
        # 'scm', 'item_name', 'wear_name', 'description', 'collection', 'badges'])

        return dict['scm']['price']
    
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


