# GW2-Inventory-API
Collate pricing and potential profit information from GW2 through use of the official API


Calculate profitability of items in:
* Character inventory
  * USAGE: character_item_profit *API key*
  
  Checks inventory of all characters on account and provides profitability of items
  
  
  * USAGE: character_item_profit *API key* --char *character name*
  
  Checks inventory of the named character on the account and provides profitability of items


* Bank inventory
  * USAGE: bank_item_profit *API key*
  
  Returns potential profits of items in account bank


* Or other misc items
  * USAGE: price_check *item id number*
  
  Returns potential profits of the indicated item
