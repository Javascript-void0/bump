import discord
import os
import asyncio
from datetime import datetime
from discord.ext import tasks, commands
from discord.utils import get

client = commands.Bot(command_prefix='.')
client.remove_command('help')
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print('Started {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(status=discord.Status.idle, type=discord.ActivityType.watching, name="Around the Clock"))

timer = False

@client.event
async def on_message(message):
    global timer
    guild = client.get_guild(802565984602423367)
    channel = guild.get_channel(802577298267963412)
    if message.author.id == 302050872383242240 and 'Check it on DISBOARD:' in message.embeds[0].description:
        embed = discord.Embed(title = "Disboard is off cooldown!", description  = "Time to bump! 🍌", color = discord.Color.dark_blue())
        embed.set_thumbnail(url="https://i.pinimg.com/originals/ee/b0/e6/eeb0e632af64b76830c5777e07770202.png")
        print('Bump Detected :D')
        cd = 7201
        print('Countdown Started')
        timer = True
        while cd > 0:
            cd -= 1
            await asyncio.sleep(1)
            print(cd)
        await channel.send(embed=embed)
        print('Reminder Sent')
        timer = False
    elif message.author.id == 594352318464524289 and '.bump' in message.content:
        if not timer:
            embed = discord.Embed(title = "Disboard is off cooldown!", description  = "Time to bump! 🍌", color = discord.Color.dark_blue())
            embed.set_thumbnail(url="https://i.pinimg.com/originals/ee/b0/e6/eeb0e632af64b76830c5777e07770202.png")
            print('Reminder Manually Started')
            timer = True
            cd = 7201
            while cd > 0:
                cd -= 1
                await asyncio.sleep(1)
                print(cd)
            await channel.send(embed=embed)
            print('Reminder Sent')
            timer = False
    await client.process_commands(message)

@tasks.loop(minutes=10.0)
async def time_check():
    global timer
    guild = client.get_guild(802565984602423367)
    channel = guild.get_channel(802577298267963412)
    message = await channel.fetch_message(channel.last_message_id)
    if message.author.id == 302050872383242240 and 'Check it on DISBOARD:' in message.embeds[0].description:
        if not timer:
            diff = datetime.utcnow() - message.created_at
            m = diff.seconds // 60
            if m > 120:
                print('Need to bump')
                embed = discord.Embed(title = "Disboard is off cooldown!", description  = "Time to bump! 🍌", color = discord.Color.dark_blue())
                embed.set_thumbnail(url="https://i.pinimg.com/originals/ee/b0/e6/eeb0e632af64b76830c5777e07770202.png")
                await channel.send(embed=embed)
                print('Reminder Sent')

@time_check.before_loop
async def before_time_check():
    print('waiting...')
    await client.wait_until_ready()

time_check.start()
client.run(TOKEN)