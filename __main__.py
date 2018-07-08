from helpers import get_bank_inventory, get_character_inventory, get_item_name

API_KEY = ''
CHARACTER_NAME = ''

inventory = get_bank_inventory(API_KEY)

for line in inventory:
    if line is None:
        print('[Blank inventory space]\n')
    else:
        name = line['id']
        amount = line['count']

        item = get_item_name(name)

        print(f'Item: {item}\nAmount: {amount}\n')

character_inventory = get_character_inventory(API_KEY, CHARACTER_NAME)

for line in character_inventory['bags']:
    for item in line['inventory']:
        if item is None:
            print('[Blank inventory space]\n')
        else:
            name = item['id']
            amount = item['count']

            item = get_item_name(name)

            print(f'Item: {item}\nAmount: {amount}\n')
