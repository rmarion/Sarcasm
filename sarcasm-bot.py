from discord.ext import commands
from discord import User
from importlib import import_module
import_module('sarcastic')
from sarcastic import change_phrase_casing


token = open('token', 'r').readline()
client = commands.Bot(command_prefix = '!')


@client.command()
async def sarcasm(ctx, arg: str):
    await ctx.send(change_phrase_casing(arg))


@client.command()
async def sarcasm_target(ctx, user: User):
    try:
        async for message in ctx.channel.history(limit=200):
            if message.author.id == user.id:
                await ctx.send(change_phrase_casing(message.content))
                return
        await ctx.send(change_phrase_casing("No recent message found for user."))
    except commands.errors.UserNotFound:
        await ctx.send(change_phrase_casing("User not found."))
    except:
        await ctx.send(change_phrase_casing("An unknown error occurred"))


client.run(token)