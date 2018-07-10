from helpers import convert_to_gold, get_all_character_inventories, get_bank_inventory, get_character_inventory, get_item_buy_price, get_item_name, get_item_profitability, get_item_sell_price

API_KEY = ''
# CHARACTER_NAME = ''

bank_inventory = get_bank_inventory(API_KEY)
# character_inventory = get_character_inventory(API_KEY, CHARACTER_NAME)

for item in bank_inventory:
    if not (item is None):

        sellable = True
        
        item_id = item['id']
        name = get_item_name(item_id)
        try:
            buy_price = get_item_buy_price(item_id)
        except KeyError:
            buy_price = 'Account bound'
            sellable = False
        except IndexError:
            buy_price = 'No buy orders'
            sellable = False

        try:
            sell_price = get_item_sell_price(item_id)
        except KeyError:
            sell_price = 'Account bound'
        except IndexError:
            sell_price = 'No sell orders'
            sellable = False

        if sellable:
            print(f'{name}\nBuy: {buy_price}\nSell: {sell_price}')

            profit = convert_to_gold(get_item_profitability(buy_price, sell_price))
            
            print(f'Flipping profit: {profit}\n')
