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
            await channel.send('Welcome {0.mention}.'.format(member))

    #on guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda x: x.name == 'general', guild.text_channels)  
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title = "Thanks for inviting me!\nBut, we need you to do somethings.", color = discord.Colour.blue())
            embed.add_field(name = "Change the muted role ID (please create a muted role if you haven't already) ", value = "By doing ``change_muted_id``. (You can change the name of the role in the code by doing ``change_muted_name``", inline = False)
            embed.add_field(name = "***Thanks for adding the discord bot!***", value = "(Thanks from -MysticRocket-)")
            embed.set_footer(text = "Finding the ID. Go to settings, Appearence, go to the bottom, and turn on 'Developer Mode'. Right click on the role or channel, and press 'copy ID' ")
            await general.send(embed = embed)







def setup(client):
    client.add_cog(EventsCog(client))