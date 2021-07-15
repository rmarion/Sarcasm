from discord.ext import commands
from importlib import import_module
import_module('sarcastic')
from sarcastic import change_phrase_casing

token = open('token', 'r').readline()
client = commands.Bot(command_prefix = '!')

@client.command()
async def sarcasm(ctx, arg):
    await ctx.send(change_phrase_casing(arg))

client.run(token)