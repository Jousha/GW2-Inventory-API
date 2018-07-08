from helpers import get_inventory, get_item_name

API_KEY = ''

inventory = get_inventory(API_KEY)

for line in inventory:
    if line is None:
        print('Blank')
    else:
        name = line['id']
        amount = line['count']

        item = get_item_name(name)

    print(f'Item: {item}\nAmount: {amount}\n')
