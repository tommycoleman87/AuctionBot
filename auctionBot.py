import os

import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
WOW_CLIENT = os.getenv('WOW_CLIENT')
WOW_SECRET = os.getenv('WOW_SECRET')

def create_access_token(client_id, client_secret):
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://us.battle.net/oauth/token', data=data, auth=(client_id, client_secret))
    return response.json()

response = create_access_token(WOW_CLIENT, WOW_SECRET)
token = response['access_token']
headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {token}'}

async def item_search(item, search_item):      
    items = requests.get(f'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&locale=en_US&name.en_US={item}&orderby=id', headers = headers)
   
    items = items.json()
    items = items['results']
    items_dict = {}
    for i in items:
        name = i['data']['name']['en_US']
        if name.find(search_item) != -1:
            items_dict[i['data']['id']] = { 'name' : i['data']['name']['en_US'], 'price' : 'Not in AH'}
    return items_dict

@bot.command(name="hello")
async def hello(message):
    await message.send(f'Hello {message.author}!')

@bot.command(name="token")
async def get_token(message):
    headers = { 'content-type': 'application/json', 'Authorization' : f'Bearer {token}'}
    token_price = requests.get(f'https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US', headers = headers)
    price = token_price.json()
    price = str(price['price'])[:-4]
    # price = price[:-4]
    user = str(message.author)
    user = user.split('#')
    user = user[0]
    await message.send(f'Hello {user}, the current price of a token is {price} gold')



@bot.command(name="price")
async def price_check(message):
    item = str(message.message.content)
    print(item)
    search_item = item[7:]
    item = item.split(' ')
    item = item[1]
    items = await item_search(item, search_item)
    auctions = requests.get(f'https://us.api.blizzard.com/data/wow/connected-realm/60/auctions?namespace=dynamic-us&locale=en_US', headers = headers)
    print(search_item)
    auctions = auctions.json()
    auctions = auctions['auctions']
    for auction in auctions:
        if auction['item']['id'] in items:
            if 'buyout' in auction:
                if auction['buyout'] < 100:
                    items[auction['item']['id']]['price'] = str(auction['buyout']) + ' copper'
                elif auction['buyout'] < 10000:
                    items[auction['item']['id']]['price'] = str(auction['buyout'])[:-2] + ' silver'
                else:
                    items[auction['item']['id']]['price'] = str(auction['buyout'])[:-4] + ' gold'

            elif 'unit_price' in auction:
                if auction['unit_price'] < 100:
                    items[auction['item']['id']]['price'] = str(auction['unit_price']) + ' copper per unit'
                elif auction['unit_price'] < 10000:
                    items[auction['item']['id']]['price'] = str(auction['unit_price'])[:-2] + ' silver per unit'
                else:
                    items[auction['item']['id']]['price'] = str(auction['unit_price'])[:-4] + ' silver per unit'
    if len(items.keys()) > 5:
        await message.send('Too many items containing that name, please be more specific')
    else:
        for i in items.keys():
            await message.send(f'{items[i]["name"]} is {items[i]["price"]}')
    




bot.run(TOKEN)