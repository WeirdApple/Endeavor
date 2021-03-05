import discord
import time
import random
from random import choice
import asyncio
from discord.ext import commands, tasks
from discord.utils import find, get
import os
import io
import datetime


status = ["me getting coded again","Almost got wiped from existence","Almost dead"]

prefixes = ['E/', 'e/']
client = commands.Bot(command_prefix = prefixes, guild_subscriptions = True, intents = discord.Intents.all())
client.remove_command("help")

@tasks.loop(seconds = 20)
async def change_status():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= random.choice(status)))

@client.event
async def on_ready():
	change_status.start()
	print("bot is ready")


#cogs
initial_extensions = ['cogs.moderation']


if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)




client.run("Nzc5MDQ5ODc5MzQ3MjY1NTM2.X7a4vQ.iNMYId3va8G-J3f92ZanlnSKzZA", bot = True, reconnect = True)
