import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTkwMjg0NjA2NDQxOTM4OTQ0.GXPASW.qsfnkdUjeksoYj8fMsJKV8pQbcH9549IHbBAN4')