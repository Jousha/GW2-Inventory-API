from helpers import get_inventory, get_item_name

inventory = get_inventory('D7E0B1A9-8A4A-AF42-920A-0564CE2DEF025E5DCC90-1E33-416F-9847-C601130B4261')

for line in inventory:
    if line is None:
        print('Blank')
    else:
        name = line['id']
        amount = line['count']

        item = get_item_name(name)

    print(f'Item: {item}\nAmount: {amount}\n')
