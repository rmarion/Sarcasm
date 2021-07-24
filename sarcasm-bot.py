from discord.ext import commands
from discord import User
from random import randint
from urllib.parse import urlparse

from importlib import import_module
import_module('sarcastic')
from sarcastic import change_phrase_casing

bot_command_prefix = '!'
auto_respond_percent_chance = 33
exclude_urls = True

token = open('token', 'r').readline()
client = commands.Bot(command_prefix = bot_command_prefix)

brief_descriptions = {
    'sarcasm': 'Makes a phrase sarcastic',
    'sarcasm_target': 'Makes the target\'s last message sarcastic'
}

help_descriptions = {
    'sarcasm': f'{bot_command_prefix}sarcasm <phrase> - states a sarcastic version of your phrase. Multiple word phrases must be contained in quotation marks.',
    'sarcasm_target': f'{bot_command_prefix}sarcasm_target @<user> - states a sarcastic version of the last message sent by <user>.'
    }

# Some messages have content that is a 404 error. There isn't any documentation on how to avoid this.
def get_safe_content_or_none(message):
    try:
        return message.content
    except:
        return None


def content_is_valid(content):
    if exclude_urls:
        return not content_is_url(content)
    return True


def content_is_url(content): # Taken from https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
    try: # Still not a huge fan of using exceptions to handle this, but it's the only validator that python themselves maintain at this point
        result = urlparse(content)
        return all([result.scheme, result.netloc])
    except:
        return False


def from_bot(message):
    return message.author.bot


@client.command(help = help_descriptions['sarcasm'], brief = brief_descriptions['sarcasm'])
async def sarcasm(ctx, phrase: str):
    await ctx.send(change_phrase_casing(phrase))
    await ctx.message.delete()


@client.command(help = help_descriptions['sarcasm_target'], brief = brief_descriptions['sarcasm_target'])
async def sarcasm_target(ctx, user: User):
    await ctx.message.delete()
    try:
        async for message in ctx.channel.history(limit=200):
            if message.author.id == user.id:
                content = get_safe_content_or_none(message)
                if content:
                    await ctx.send(change_phrase_casing(message.content))
                    return
        await ctx.send(change_phrase_casing('No recent message found for user.'))
    except commands.errors.UserNotFound:
        await ctx.send(change_phrase_casing('User not found.'))
    except:
        await ctx.send(change_phrase_casing('An unknown error occurred.'))


@client.event
async def on_message(message):
    if from_bot(message):
        return
    if randint(1, auto_respond_percent_chance) == 1:
        channel = message.channel
        content = get_safe_content_or_none(message)
        if content and content_is_valid(content):
            await channel.send(change_phrase_casing(content))
    await client.process_commands(message)


client.run(token)