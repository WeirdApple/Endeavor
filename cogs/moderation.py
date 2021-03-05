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


class ModerationCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    #clear
    @commands.command(aliases = ['CLEAR'])
    async def clear(self, ctx, amount : int):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        await ctx.send(f"Messages in {ctx.channel} go brrrrrr!", delete_after = 0.8)
        

    #whois
    @commands.command(aliases = ['WHOIS','userinfo'])
    @commands.has_permissions(kick_members = True)
    async def whois(self, ctx, member : discord.Member):
        embed = discord.Embed(title = member.name , decription = member.display_name , color = discord.Colour.green())
        embed.add_field(name = "ID", value = member.id, inline = True)
        embed.add_field(name = "Is bot?", value = member.bot, inline = True)
        embed.add_field(name = "Is your friend?", value = member.is_friend(), inline = True)
        embed.add_field(name = "Account Creation", value = member.created_at, inline = True)
        embed.add_field(name = "Default avatar url link", value = member.default_avatar_url, inline = True)
        embed.add_field(name = "Highest Role", value = member.top_role.name)

        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        embed.add_field(name = "Permissions", value = perms)

        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)
        

    #Server Info
    @commands.command(aliases=["si"])

    async def serverinfo(self, ctx): 
        embed = discord.Embed(title = f"Stats for {ctx.guild.name}", description = "", color = discord.Color.green())
        embed.set_thumbnail(url = f"{ctx.guild.icon_url}")
        embed.add_field(name = ":crown: Owner of Server", value =  ctx.guild.owner)
        embed.add_field(name = ":earth_americas: Region", value = f"{ctx.guild.region}")
        embed.add_field(name = "<:peopleemoji:771797557452996608> Member Count", value = f"{ctx.guild.member_count}")
        embed.add_field(name = ":calendar: Created at (UTC)", value = f"{ctx.guild.created_at}")
        embed.add_field(name = "ID", value = f"{ctx.guild.id}")
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    #get channel
    @commands.command()
    async def get_channel(self, ctx, *, given_name = "None"):

        for channel in ctx.guild.channels:
            if channel.name == given_name:
                wanted_channel_id = channel.id

        await ctx.send(wanted_channel_id)


def setup(client):
    client.add_cog(ModerationCog(client))