# config.py (Python)

import discord
from discord.ext import commands
import asyncio
import requests
import json

# Define your Discord bot token here
TOKEN = 'your_bot_token_here'

# Create a new Discord bot instance
bot = commands.Bot(command_prefix='!')

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Add your bot commands here
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello! I am your Discord moderation bot.')

# Run the bot with the specified token
bot.run(TOKEN)