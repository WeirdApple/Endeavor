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


class OtherCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    #invite link
    @commands.command(aliases = ['INVITE','Invite'])
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=779049879347265536&permissions=8&scope=bot")
        

    #create poll
    @commands.command(aliases = ["CREATEPOLL","CP","Createpoll","cp", 'poll'])
    @commands.has_permissions(manage_guild = True)
    async def createpoll(self, ctx,*, poll):
        channel = get(ctx.guild.text_channels, name='polls')

        await ctx.message.delete()
        await ctx.send("Sent! Go check #polls")
        emb = discord.Embed(title = f"Poll created by {ctx.author.name}", description = f"{poll}",color = discord.Colour.dark_green())
        emb.set_thumbnail(url = ctx.author.avatar_url)
        msg = await channel.send(embed = emb)
        await msg.add_reaction("\U0001f1fe")
        await msg.add_reaction("\U0001f1f3")


    #suggestions
    @commands.command(aliases = ['SUGGEST','sgst','Suggest','SGST','Sgst'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def suggest(self, ctx,*, suggestion):
        channel = get(ctx.guild.text_channels, name='suggestions')
        await ctx.message.delete()
        await ctx.send("Sent! Go check #suggestions")
        em = discord.Embed(title = f"Suggestion by {ctx.author.name}", description = f"{suggestion}",color = discord.Colour.dark_green())
        msg = await channel.send(embed = em)
        await msg.add_reaction("\U00002705")
        await msg.add_reaction("\U0000274c")




def setup(client):
    client.add_cog(OtherCog(client))