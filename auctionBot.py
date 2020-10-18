import os

import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
from auctionBot_class import AuctionBot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
WOW_CLIENT = os.getenv('WOW_CLIENT')
WOW_SECRET = os.getenv('WOW_SECRET')
token = ''
server_name = 'Stormrage'
server_id = 60
guilds = {}

@bot.command(name='hello')
async def hello(ctx):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].greet(ctx)
    else:
        await guilds[f'{guild}'].greet(ctx)

@bot.command(name='server')
async def server(ctx):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].current_server(ctx)
    else:
        await guilds[f'{guild}'].current_server(ctx)

@bot.command(name='setserver')
async def setserver(ctx, *, arg):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].set_server(ctx, arg)
    else:
        await guilds[f'{guild}'].set_server(ctx, arg)
@bot.command(name='guilds')
async def guilds_print(ctx):
    await ctx.send(guilds)

# def create_access_token(client_id, client_secret):
#     data = { 'grant_type': 'client_credentials' }
#     response = requests.post('https://us.battle.net/oauth/token', data=data, auth=(client_id, client_secret))
#     return response




# async def item_search(item, search_item): 
#     headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {token}'}     
#     items = requests.get(f'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&locale=en_US&name.en_US={item}&orderby=id', headers = headers)
#     items = items.json()
#     items = items['results']
#     items_dict = {}
#     for i in items:
#         name = i['data']['name']['en_US']
#         if name.find(search_item) != -1:
#             items_dict[i['data']['id']] = { 'name' : i['data']['name']['en_US'], 'price' : 'Not in AH'}
#     return items_dict

# @bot.command(name="login")
# async def login(message):
#     response = create_access_token(WOW_CLIENT, WOW_SECRET)
#     if response.status_code != 200:
#         await message.send(f'Network error {response.status_code}')
#     else:
#         global token
#         response = response.json()
#         if 'access_token' in response:
#             token = response['access_token']
#         else:
#             await message.send(f'network error {response}')

# @bot.command(name="hello")
# async def hello(message):
#     await message.send(f'Hello {message.author}!')

# @bot.command(name="token")
# async def get_token(message):
#     headers = { 'content-type': 'application/json', 'Authorization' : f'Bearer {token}'}
#     token_price = requests.get(f'https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US', headers = headers)
#     if token_price.status_code == 200:
#         price = token_price.json()
#         price = str(price['price'])[:-4]
#         user = str(message.author)
#         user = user.split('#')
#         user = user[0]
#         await message.send(f'Hello {user}, the current price of a token is {price} gold')
#     elif token_price.status_code == 401:
#         await login(message)
#         await get_token(message)
#     else:
#         await message.send(f'Network error {token_price.status_code}')
        

# @bot.command(name="price")
# async def price_check(message):
#     item = str(message.message.content)
#     print(item)
#     search_item = item[7:]
#     item = item.split(' ')
#     item = item[1]
#     items = await item_search(item, search_item)
    
#     headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {token}'}
#     auctions = requests.get(f'https://us.api.blizzard.com/data/wow/connected-realm/{server_id}/auctions?namespace=dynamic-us&locale=en_US', headers = headers)
#     if auctions.status_code == 401:
#         await login(message)
#         await price_check(message)
#     elif auctions.status_code == 200:
#         auctions = auctions.json()
#         auctions = auctions['auctions']
#         for auction in auctions:
#             if auction['item']['id'] in items.keys():
#                 if 'buyout' in auction:
#                     if auction['buyout'] < 100:
#                         items[auction['item']['id']]['price'] = str(auction['buyout']) + 'Copper'
#                     elif auction['buyout'] < 10000:
#                         items[auction['item']['id']]['price'] = str(auction['buyout'])[:-2] + 'Silver ' + str(auction['buyout'])[-2:] + 'Copper'
#                     else:
#                         items[auction['item']['id']]['price'] = str(auction['buyout'])[:-4] + 'Gold ' + str(auction['buyout'])[-4:-2] + "Silver " + str(auction['buyout'])[-2:] + 'Copper'

#                 elif 'unit_price' in auction:
#                     if auction['unit_price'] < 100:
#                         items[auction['item']['id']]['price'] = str(auction['unit_price']) + 'Copper Per Unit'
#                     elif auction['unit_price'] < 10000:
#                         items[auction['item']['id']]['price'] = str(auction['unit_price'])[:-2] + 'Silver ' + str(auction['unit_price'])[-2:] + 'Copper Per Unit'
#                     else:
#                         items[auction['item']['id']]['price'] = str(auction['unit_price'])[:-4] + 'Gold ' + str(auction['unit_price'])[-4:-2] + 'Silver ' + str(auction['unit_price'])[-2:] + "Copper Per Unit"
#         if len(items.keys()) > 5:
#             await message.send('Too many items containing that name, please be more specific')
#         elif len(items.keys()) == 0:
#             await message.send(f'No auctions found for {search_item}')
#         else:
#             for i in items.keys():
#                 await message.send(f'{items[i]["name"]} is {items[i]["price"]}')
#     else:
#         await message.send(f'Network error {auctions.status_code}')

# @bot.command(name="servercheck")
# async def servercheck(message):
#     await message.send(f'The current server is set to {server_name}')

# @bot.command(name='server')
# async def server_change(message):
#     headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {token}'}
#     realm = str(message.message.content).split(' ')[1]
#     get_realm = requests.get(f'https://us.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-us&realms.name.en_US={realm}', headers = headers)
#     if get_realm.status_code != 200:
#         await message.send(f'Network error, status code {get_realm.status_code}')
#     else:
        
#         get_realm = get_realm.json()['results']
#         if len(get_realm) > 1:
#             await message.send('Please check the spelling of the server or be more specific')
#         elif len(get_realm) == 0:
#             await message.send('Server not found, please check spelling')
#         else:
#             global server_name
#             global server_id
#             server_name = get_realm[0]['data']['realms'][0]['name']['en_US']
#             server_id = get_realm[0]['data']['id']
#             await message.send(f'Server set to {server_name}, id {server_id}')


    




bot.run(TOKEN)