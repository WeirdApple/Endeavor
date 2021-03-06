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


class FunCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fban(self, ctx, member : discord.Member = None,*, reason="Not given"):

        if member == None:
            await ctx.send("mention the person to ban you dumbo")
            return 
        embed = discord.Embed(title = f"*{member} banned successfully   :white_check_mark:*", description = f"Reason: {reason}", colour=0x8c9eff, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
        await ctx.message.delete()


    #roasts
    @commands.command(aliases = ['ROAST','insult','INSULT','Roast','Insult'])
    async def roast(ctx, member : discord.Member = None):
        if not member:
            member = ctx.author

        with open("roasts.txt","r") as f:
            for line in f:
                roast = random.choice(line)
                print(line)

        embed = discord.Embed(title = f"Here is a roast for {member.name}...", description = roast, color = discord.Color(0xff55ff))
        embed.add_field(name = "There you go.", value = "HaHa")
        await ctx.send(embed = embed)

    #RPS GAME
    @commands.command(aliases = ['RPS','rps','Rockpaperscissors'])
    async def rockpaperscissors(self, ctx, *, choose = None):
        CPUChoose = ['rock','paper','scissors']
        chooselistscissors = ['SCISSORS','Scissors']
        CPUchoose = random.choice(CPUChoose)
            #rocks
        if CPUchoose == "rock" and choose == "rock":
            embed = discord.Embed(title = "IT WAS A TIE!", description = "Try again to win!", color = discord.Color(0xff55ff))
            await ctx.send(embed = embed)
        if CPUchoose == "rock" and choose == "paper":
            embed = discord.Embed(title = "YOU WON!", description = "Try again to win again!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose rock", value = ":rock:")
            await ctx.send(embed = embed)
        if CPUchoose == "rock" and choose == "scissors":
            embed = discord.Embed(title = "YOU LOST!", description = "Try again to win!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose rock", value = ":rock:")
            await ctx.send(embed = embed)
        #paper
        if CPUchoose == "paper" and choose == "paper" :
            embed = discord.Embed(title = "IT WAS A TIE!", description = "Try again to win!", color = discord.Color(0xff55ff))
            await ctx.send(embed = embed)
        if CPUchoose == "paper" and choose == "rock":
            embed = discord.Embed(title = "YOU LOST!", description = "Try again to win!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose paper", value = ":newspaper:")
            await ctx.send(embed = embed)
        if CPUchoose == "paper" and choose == "scissors":
            embed = discord.Embed(title = "YOU WIN!", description = "Try again to win again!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose paper", value = ":newspaper:")
            await ctx.send(embed = embed)
        #scissors
        if CPUchoose == "scissors" and choose == "scissors":
            embed = discord.Embed(title = "IT WAS A TIE!", description = "Try again to win!", color = discord.Color(0xff55ff))
            await ctx.send(embed = embed)
        if CPUchoose == "scissors" and choose == "paper":
            embed = discord.Embed(title = "YOU LOST!", description = "Try again to win!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose scissors", value = ":scissors:")
            await ctx.send(embed = embed)

        if CPUchoose == "scissors" and choose == "rock":
            embed = discord.Embed(title = "YOU WON!", description = "Try again to win again!", color = discord.Color(0xff55ff))
            embed.add_field(name = "The Computer chose scissors", value = ":scissors:")
            await ctx.send(embed = embed)
        #error
        if not choose:
            await ctx.send("Choose a valid word. ``rock``, ``paper``, or ``scissors``")
            #finish up
	

	

    #add to help
    #say
    @commands.command(aliases = ['Say','SAY'])
    async def say(self, ctx, *, message):
        await ctx.send(f"{message}")


    #STFU PERSON
    @commands.command(aliases = ['STFU'])
    async def stfu(self, ctx, member : discord.Member):
        await ctx.send(f"***STFU {member.mention}!***")

    #8ball  
    @commands.command(aliases = ['8BALL','8Ball','8ball'])
    async def _8ball(self, ctx):
        eightball_list = ['As I see it, yes.','Ask again later.',' Better not tell you now.',' Cannot predict now.',' Concentrate and ask again.',' Don’t count on it.',' It is certain.',' It is decidedly so.',' Most likely.',' My reply is no.',' My sources say no.']
        await ctx.send(f"{random.choice(eightball_list)}")

    #duce easteregg
    @commands.command(aliases = ['DUCE'])
    async def duce(self, ctx):
        await ctx.send("You mean ``e/die``? Cuz the El Duce was Benito Mussolini. Are you a fascist?")



    #dice
    @commands.command(aliases = ['DIE', 'Die','DICE','Dice','dice'])
    async def die(self, ctx, die = 6):
        die = random.randint(1,die)
        embed = discord.Embed(title = f"{ctx.author.name} is rolling a die", description = f"{ctx.author.name} got {die}", color = discord.Colour(0xff55ff))
        embed.set_footer(text = "FYI, one dice is 'die', 2 or more dies are 'dice'. Remember that")
        await ctx.send(embed= embed)


    #howgay
    @commands.command(aliases = ['HOWGAY','Howgay'])
    async def howgay(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        gaycount = random.randint(0,100)
        embed = discord.Embed(title = f"Let's see how gay {member.name} is. :rainbow_flag:", description = f"{gaycount}%", color = discord.Color(0xff55ff))
        await ctx.send(embed = embed)

    #flip a coin
    @commands.command(aliases = ['COINFLIP','Coinflip'])
    async def coinflip(self, ctx):
        twocoins = ['Heads','Tails']
        embed = discord.Embed(title = f"{ctx.author.name} is flipping a coin...", description = f"{ctx.author.name} got {random.choice(twocoins)}", color = discord.Colour(0xff55ff))
        await ctx.send(embed = embed)
        #fix

    #sus level
    @commands.command(aliases = ["HOWSUS", "Howsus"])
    async def howsus(self, ctx, member: discord.Member = None):
        suslist = ['Very', 'No', 'Definitely not', 'Red level sus', 'How is he sus?', 'Probably', 'Good Chance', 'Cyan level Sus','Why is he or she sus?','``ERROR 404, SUS OVERLOAD``', 'Yes, ofc', 'Yes','No?', 'Why he or she?']
        if not member:
            member = ctx.author

        embed = discord.Embed(title = f"How sus is {member.name}?", description = "LET'S FIND OUT!",color = discord.Colour(0xff55ff))
        embed.add_field(name = "Is sus?", value = f"{random.choice(suslist)}",inline = False)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

        await ctx.send(embed = embed)

    #when will die
    @commands.command(aliases = ["WHENDIE", "Whendie"])
    async def whendie(self, ctx, member: discord.Member = None):
        dielist = ['seconds','minutes','hours','days','weeks','months','years','centuries']
        if not member:
            member = ctx.author

        embed = discord.Embed(title = f"When will {member.name} die?", description = "LET'S FIND OUT!",color = discord.Colour(0xff55ff))
        numberdie = random.randint(1,50)
        embed.add_field(name = "When will he/she die??", value = f"{numberdie} {random.choice(dielist)}",inline = False)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

        await ctx.send(embed = embed)



    #lovetest
    @commands.command(aliases = ['LOVETEST','Lovetest','LoveTest'])
    async def lovetest(self, ctx, lover1 = None, lover2 = None):
        muchlove = random.randint(0,100)
        embed = discord.Embed(title = f"{ctx.author.name} is seeing if {lover1} and {lover2} really love eachother! :heart:", description = f"Lets see what happens!", color = discord.Color(0xff55ff))
        embed.add_field(name = f"The percentage of love is{muchlove}%", field = "yeee")
        embed.set_footer(text = "If it's 50 percent and lower, they aren't supposed to be with eachother")
        await ctx.send(embed= embed)




def setup(client):
    client.add_cog(FunCog(client))