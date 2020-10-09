import os

import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
# from oauth_hook import OAuthHook

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

@bot.command(name="search")
async def item_search(message):
    print(message.content)







bot.run(TOKEN)