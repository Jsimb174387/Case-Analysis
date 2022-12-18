import requests
from settings import keyRet
from time import sleep
import json
import pyotp

#guide to requests:
# payload = {'paint_index': '695', 'sort_by': 'lowest_price', 'limit': '1', 'type': 'buy_now'}
# data = requests.get("https://csgofloat.com/api/v1/listings", params = payload)
# dict = data.json()[0]
# print(dict['price'])

def ret_ref_prices():
    #https://bitskins.com/api/v1/get_all_item_prices/?api_key=API_KEY&code=CODE&app_id=APP_ID
    api_key = input('Bitskins API Key: ')
    code = input('security code: ')
    req = 'https://bitskins.com/api/v1/get_all_item_prices/?api_key=' + api_key + '&code=' + code
    data = requests.get(req)
    market = data.json()

    with open('ref_prices.json', 'w') as outfile:
        json.dump(market, outfile)

def secure_code(secret = None):
    # get a token that's valid right now
    if secret == None:
        my_secret = input('input secret')
        my_token = pyotp.TOTP(my_secret)
    else:
        my_token = pyotp.TOTP(secret)
    # return the valid token
    print(my_token.now())
    return(my_token.now())

def get_ref_info(hash):
    f = open('ref_prices.json',)
    market_data = json.load(f)
    for skin in market_data['prices']:
        if skin['market_hash_name'] == hash:
            return skin['price']
def ret_market_data():
    # https://bitskins.com/api/v1/get_all_item_prices/?api_key=API_KEY&code=CODE&app_id=APP_ID
    api_key = input('Bitskins API Key: ')
    code = input('security code: ')
    req = 'https://bitskins.com/api/v1/get_price_data_for_items_on_sale/?api_key=' + api_key + '&code=' + code
    data = requests.get(req)
    market = data.json()

    with open('market_prices.json', 'w') as outfile:
        json.dump(market, outfile)

def get_market_info(hash):
    f = open('market_prices.json',)
    market_data = json.load(f)
    for skin in market_data['data']['items']:
        if skin['market_hash_name'] == hash:
            return [skin['lowest_price'], skin['total_items']]
    return ['item not found','item not found']


#get_market_info('AK-47 | Uncharted (Field-Tested)')
# f= get_market_info('AK-47 | Uncharted (Field-Tested)')
# print(f)