import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content[0] == '!':
        await message.channel.send(f'Hello {message.author}')

client.run(TOKEN)