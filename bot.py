import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot


TOKEN = 'NTE2ODgyOTExODI0MzE0MzY4.Dt6I9A.F_bMDgeE8XxVmt0UBvduX0GlLRg'

startup_extensions = ["music"]
BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hello',
                description="answers your greetings",
                brief="Answers from the beyond.",
                aliases=['yo', 'hey', 'hello'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'hey',
        'nice day',
        'good to see you',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))



client.run(TOKEN)
