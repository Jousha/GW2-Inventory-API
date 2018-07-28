import click
from helpers import convert_to_gold
from helpers import get_item_name, get_item_profitability
from helpers import get_item_buy_price, get_item_buy_strength, get_item_sell_price, get_item_sell_strength

'''
Input:
    The id number of an item in the game

Returns:
    The potential profit from flipping the input item on the auction house
'''

@click.command()
@click.option('--item_id', default='1', help='item id to return item name')
@click.argument('item_id')
def get_item_profit(item_id):
    try:
        name = get_item_name(item_id)
        profit = convert_to_gold(get_item_profitability(item_id))

        buy_price = get_item_buy_price(item_id)
        buy_strength = get_item_buy_strength(item_id)
        sell_price = get_item_sell_price(item_id)
        sell_strength = get_item_sell_strength(item_id)
    
        click.echo(f'{item_id} is {name}')
        click.echo(f'Potential: {profit}\n')
        click.echo('Stats:')
        click.echo(f'Current buying price: {buy_price}')
        click.echo(f'Current orders at this price: {buy_strength}')
        click.echo(f'Current selling price: {sell_price}')
        click.echo(f'Current orders at this price: {sell_strength}\n')

    except KeyError:
        click.echo('Please provide a valid id\n')

if __name__ == '__main__':
    get_item_profit()
