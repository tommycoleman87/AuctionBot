import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from auctionBot_class import AuctionBot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

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

@bot.command(name='token')
async def token_price(ctx):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].token(ctx)
    else:
        await guilds[f'{guild}'].token(ctx)

@bot.command(name='price')
async def price(ctx, *, arg):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].price_check(ctx, arg)
    else:
        await guilds[f'{guild}'].price_check(ctx, arg)

@bot.command(name='guilds')
async def guilds_print(ctx):
    await ctx.send(guilds.keys())


        

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






    




bot.run(TOKEN)