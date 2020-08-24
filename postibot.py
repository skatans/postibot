import os
import discord
import subprocess
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PATH = os.getenv('DIRECTORY_PATH')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to:\n'
        f'{guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'onk postii' in message.content or message.content == '!posti':
        subprocess.call([PATH+'/webcam.sh'])
        await message.channel.send(file=discord.File(PATH+'posti.jpg'))


client.run(TOKEN)
