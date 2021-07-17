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
    oldest_message = await get_oldest_message(ctx, user.id)
    await ctx.send(change_phrase_casing(oldest_message))


async def get_oldest_message(ctx, id):
    messages = await ctx.channel.history(limit=200)
    user_messages = [message for message in messages if message.author.id == id]
    if not user_messages:
        return "No recent message found for user."
    return user_messages[-1]


client.run(token)