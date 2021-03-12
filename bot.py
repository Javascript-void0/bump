import discord
import asyncio
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.atc ')
TOKEN = os.getenv("DIS_TOKEN")

@client.event
async def on_ready():
    print('Started {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Around the Clock"))

@client.event
async def on_message(message):
    embed = discord.Embed(title = "Disboard is off cooldown!", description  = "Time to bump! 🍌", color = discord.Color.dark_blue())
    embed.set_thumbnail(url="https://i.pinimg.com/originals/ee/b0/e6/eeb0e632af64b76830c5777e07770202.png")
    channel = message.channel
    if message.author.id == 302050872383242240 and 'done' in message.embeds[0].description:
        cd = 7201
        while cd >= 0:
            cd = cd-5
            await asyncio.sleep(5)
            if cd == 0:
                await channel.send(embed=embed)
    else:
        pass

if __name__ == '__main__':
    client.run(TOKEN)