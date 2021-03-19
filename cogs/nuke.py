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


class NukeCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "nuke")
    async def nuke(self, ctx):
        await ctx.send("dropping nuke...")




def setup(client):
    client.add_cog(NukeCog(client))



