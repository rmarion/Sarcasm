from discord.ext import commands
from discord import User
from importlib import import_module
import_module('sarcastic')
from sarcastic import change_phrase_casing


token = open('test-token', 'r').readline()
client = commands.Bot(command_prefix = '!')


@client.command()
async def sarcasm(ctx, arg: str):
    await ctx.send(change_phrase_casing(arg))
    await ctx.message.delete()


@client.command()
async def sarcasm_target(ctx, user: User):
    await ctx.message.delete()
    try:
        async for message in ctx.channel.history(limit=200):
            if message.author.id == user.id:
                try: # Some messages have content that is a 404 error. There isn't any documentation on how to avoid this.
                    await ctx.send(change_phrase_casing(message.content))
                    return
                except:
                    continue
        await ctx.send(change_phrase_casing('No recent message found for user.'))
    except commands.errors.UserNotFound:
        await ctx.send(change_phrase_casing('User not found.'))
    except:
        await ctx.send(change_phrase_casing('An unknown error occurred.'))


client.run(token)