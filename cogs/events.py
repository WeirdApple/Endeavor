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


class EventsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    #on member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title = "Welcome {0.mention}!", description = f"We hope you have a good time in {member.guild.name}!")
            embed.add_field(name = "Please don't leave", field = ":(")
            await channel.send('Welcome {0.mention}!'.format(member))

    #on guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda x: x.name == 'general', guild.text_channels)  
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title = "Thanks for inviting me!", description = "Go check my GitHub open source [here!](https://github.com/WeirdApple/Endeavor)",color = discord.Colour.blue())







def setup(client):
    client.add_cog(EventsCog(client))