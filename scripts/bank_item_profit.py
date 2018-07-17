import click
from helpers import convert_to_gold, get_bank_inventory
from helpers import get_item_buy_price, get_item_name, get_item_profitability, get_item_sell_price

'''
Input:
    The API key of an account in the game

Returns:
    The potential profit of all tradeable items in the bank
'''

@click.command()
@click.option('--api_key', help='account api key from guild wars 2 site')
@click.argument('api_key')
def get_bank_profit(api_key):
    bank_inventory = get_bank_inventory(api_key)

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
                click.echo(f'{name}\nBuy: {buy_price}\nSell: {sell_price}')

                profit = convert_to_gold(get_item_profitability(item_id))
                
                click.echo(f'Flipping potential: {profit}\n')

if __name__ =='__main__':
    get_bank_profit()
