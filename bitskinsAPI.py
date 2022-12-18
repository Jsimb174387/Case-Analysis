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

def ret_prices():
    #https://bitskins.com/api/v1/get_all_item_prices/?api_key=API_KEY&code=CODE&app_id=APP_ID
    api_key = input('Bitskins API Key: ')
    code = input('security code: ')
    req = 'https://bitskins.com/api/v1/get_all_item_prices/?api_key=' + api_key + '&code=' + code
    data = requests.get(req)
    market = data.json()

    with open('price_data.json', 'w') as outfile:
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

ret_prices()