import json
import math
import requests

def get_bank_inventory(api_token):
    '''
    Input:
        api_token - String of the api key of a valid account with inventory viewing rights

    Returns a list object containing the bank inventory associated with the api key
    '''
    inventory_api = f'https://api.guildwars2.com/v2/account/bank?access_token={api_token}'
    return _parse_data(inventory_api)

def get_character_inventory(api_token, character_name):
    '''
    Input:
        api_token - String of the api key of a valid account with inventory viewing rights
        character_name - The name of the character which will be queried

    Returns a list object containing the character inventory associated with the api key
    '''
    if (' ' in character_name):
        character_name = '%20'.join(character_name.split(' '))
        
    character_api = f'https://api.guildwars2.com/v2/characters/{character_name}/inventory?access_token={api_token}'
    return _parse_data(character_api)

def get_all_character_inventories(api_token):
    '''
    Input:
        api_token - String of the api key of a valid account with inventory viewing rights

    Returns a dictionary object of [Key] Character name: [Value] Inventory{list)
    '''
    character_list_api = f'https://api.guildwars2.com/v2/characters?access_token={api_token}'
    characters = _parse_data(character_list_api)

    character_inventories = {}

    for character in characters:
        character_inventories[character] = get_character_inventory(api_token, character)

    return character_inventories

def get_item_name(item_id):
    '''
    Input:
        item_id - String of an id reference number of an item in the game

    Returns a string object for the item's name
    '''
    item_api = f'https://api.guildwars2.com/v2/items?ids={item_id}'
    item_data = _parse_data(item_api)
    return item_data[0]['name']

def get_item_buy_price(item_id):
    '''
    Input:
        item_id - String of an id reference number of an item in the game

    Returns a string object for the item's auction house sell price (in copper)
    '''
    item_api = f'https://api.guildwars2.com/v2/commerce/listings?ids={item_id}'
    price_list = _parse_data(item_api)
    return price_list[0]['buys'][0]['unit_price']
    

def get_item_sell_price(item_id):
    '''
    Input:
        item_id - String of an id reference number of an item in the game

    Returns a string object for the item's auction house buy price (in copper)
    '''
    item_api = f'https://api.guildwars2.com/v2/commerce/listings?ids={item_id}'
    price_list = _parse_data(item_api)
    return price_list[0]['sells'][0]['unit_price']

def get_item_profitability(item_id):
    '''
    Input:
        item_id - String of an id reference number of an item in the game

    Returns an integer object of the expected profit from flipping the item
    after transaction fees (5% on listing and 10% on sale) have been taken
    '''
    cost = 0
    revenue = 0

    buy = get_item_buy_price(item_id)
    sell = get_item_sell_price(item_id)
    
    if (buy * 0.05) < 1:
        cost = buy + 1
    else:
        cost = math.ceil(buy * 1.05)

    if (sell * 0.10) < 1:
        revenue = sell - 1
    else:
        revenue = math.floor(sell * 0.90)
        
    return revenue - cost

def convert_to_gold(amount):
    '''
    Input:
        amount - An amount of money (in coppers)

    Returns a string representation of the given amount in gold, silver, copper format
    '''
    negative = False
    if amount < 0:
        negative = True
        amount = abs(amount)
    
    if amount < 100:
        if negative:
            return f'{amount}c loss'
        else:
            return f'{amount}c profit'
    elif amount < 1000:
        silver = math.floor(amount / 100)
        copper = amount % 100
        if negative:
            return f'{silver}s {copper}c loss'
        else:
            return f'{silver}s {copper}c profit'
    else:
        gold = math.floor(amount / 1000)
        silver = math.floor((amount % 1000) / 100) 
        copper = (amount % 1000) % 100
        if negative:
            return f'{gold}g {silver}s {copper}c loss'
        else:
            return f'{gold}g {silver}s {copper}c profit'
    

def _parse_data(api_string):
    '''
    Input:
        api_string - String of a valid api link

    Returns a list object of JSON parsed data from the api link
    '''
    r = requests.get(api_string)
    parsed_r = json.loads(r.text)
    return parsed_r

