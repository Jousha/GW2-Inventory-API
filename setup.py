from setuptools import setup

setup(
    name='price_check',
    version='1.0',
    py_modules=['price_check', 'bank_item_profit', 'get_character_profit'],
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        price_check=price_check:get_item_profit
        bank_item_profit=bank_item_profit:get_bank_profit
        character_item_profit=character_item_profit:get_character_profit
    ''',
)
