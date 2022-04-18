token = "OTY1MzcwMDQ1Nzc5ODA4MzQ3.YlyM6g.mg0zniMV_32A9tcaor47OKZCS2E" #This is the token generated with discord!

#imports!

import discord
from discord.ext import commands

#setup


bot = discord.Client() #intializes the bot
prefix = '!'  #the prefix of the bot! Its essential to function

bot = commands.Bot(command_prefix=prefix) #set the prefix
bot.remove_command('help') #remove the default help command because we want to create our own

#on ready

@bot.event
async def on_ready():
    print("Bot is running!")

#first command /help

@bot.command()
async def help(ctx):
    print("User requestsed help command")
    await ctx.send("This is the help command!")

#second command

@bot.command()
async def status(ctx):
    print("User requested status")
    await ctx.send("The Bot is ONLINE!!")
#run

bot.run(token) #run the bot with the token we entered at the beggining

