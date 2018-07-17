import click
from helpers import convert_to_gold
from helpers import get_item_name, get_item_profitability

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
    
        click.echo(f'{item_id} is {name}')
        click.echo(f'Potential: {profit}')

    except KeyError:
        click.echo('Please provide a valid id')

if __name__ == '__main__':
    get_item_profit()
