import os
import random
import discord
from discord.ext import tasks, commands

user_token = os.environ['user_token']
spam_id = os.environ['spam_id']

client = commands.Bot(command_prefix='Lickitysplit')
intervals = [2.8, 3.0, 3.2, 3.8]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    if channel:
        await channel.send(''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 7) * 5))

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')

@client.command()
async def start(ctx):
    """Starts the spam task."""
    if not spam.is_running():
        spam.start()
        await ctx.send("Spam task started!")
    else:
        await ctx.send("Spam task is already running.")

@client.command()
async def stop(ctx):
    """Stops the spam task."""
    if spam.is_running():
        spam.cancel()
        await ctx.send("Spam task stopped!")
    else:
        await ctx.send("Spam task is not running.")

client.run(user_token)
