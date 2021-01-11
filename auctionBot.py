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

@bot.command(name='search')
async def search(ctx, *, arg):
    guild = str(ctx.guild)
    if guild not in guilds:
        guilds[f'{guild}'] = AuctionBot()
        await guilds[f'{guild}'].item_search(ctx, arg)
    else:
        await guilds[f'{guild}'].item_search(ctx, arg)
@bot.command(name='commands')
async def commands_list(ctx):
    await ctx.send('Commands are: \n !price <item name> - returns the auction price of the item in the current server \n !setserver <server name> - sets the bot to the server \n !server - returns the current server \n !token - returns the current price of a wow token \n !hello - greets the user')

@bot.command(name='guilds')
async def guilds_print(ctx):
    await ctx.send(guilds.keys())
    await ctx.send(bot.user)
bot.run(TOKEN)