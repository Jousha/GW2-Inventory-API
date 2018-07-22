import click
from helpers import get_character_inventory, get_all_character_inventories
from helpers import get_item_name, get_item_profitability, convert_to_gold

'''
Input:
    The API key of an account in the game
    Optional: Name of a character on the account

Returns:
    If a name is given, the priced inventory of the named character
    Otherwise, all character priced inventories 
'''

@click.command()
@click.option('--char', default='', help='character name to be searched')
@click.argument('api_key')
def get_character_profit(api_key, char):
    if char == '':
        inventories = get_all_character_inventories(api_key)
        for character in inventories.keys():
            click.echo(f'{character}:')
            for item_id in inventories[character]:
                try:
                    name = get_item_name(item_id)
                    profit = convert_to_gold(get_item_profitability(item_id))
                    click.echo(f'{name}\n{profit}\n')
                except:
                    continue
            click.echo('\n')
    else:
        try:
            inventory = get_character_inventory(api_key, char)
            click.echo(f'{char}:')
            for item_id in inventory:
                try:
                    name = get_item_name(item_id)
                    profit = convert_to_gold(get_item_profitability(item_id))
                    click.echo(f'{name}\n{profit}\n')
                except:
                    continue
            click.echo('\n')
        except KeyError:
            click.echo('Invalid character name or API key')
    
if __name__ == '__main__':
    get_character_profit()
