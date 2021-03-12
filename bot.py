import discord
import os
import asyncio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='??')
TOKEN = os.getenv("DIS_TOKEN")

@client.event
async def on_ready():
    print('Started {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.watching, name="Around the Clock"))

@client.event
async def on_message(message):
    embed = discord.Embed(title = "Disboard is off cooldown!", description  = "Time to bump! 🍌", color = discord.Color.dark_blue())
    embed.set_thumbnail(url="https://i.pinimg.com/originals/ee/b0/e6/eeb0e632af64b76830c5777e07770202.png")
    guild = client.get_guild(802565984602423367)
    channel = guild.get_channel(802577298267963412)
    if message.author.id == 302050872383242240 and 'done' in message.embeds[0].description:
        print('Bump Detected :D')
        cd = 7201
        print('Countdown Started')
        while cd >= 0:
            cd -= 1
            await asyncio.sleep(1)
            print(cd)
        await channel.send(embed=embed)
        print('Reminder Sent')

client.run(TOKEN)