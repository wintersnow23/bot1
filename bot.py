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

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))



client.run(TOKEN)
