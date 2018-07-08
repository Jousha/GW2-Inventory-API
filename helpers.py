import json
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

def get_item_name(item_id):
    '''
    Input:
        item_id - String of an id reference number of an item in the game

    Returns a string object for the item's name
    '''
    item_api = f'https://api.guildwars2.com/v2/items?ids={item_id}'
    item_data = _parse_data(item_api)
    return item_data[0]['name']

def _parse_data(api_string):
    '''
    Input:
        api_string - String of a valid api link

    Returns a list object of JSON parsed data from the api link
    '''
    r = requests.get(api_string)
    parsed_r = json.loads(r.text)
    return parsed_r
