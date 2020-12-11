import discord
import os
from utils import logs
from utils import config
from discord.ext import commands

client = commands.Bot(command_prefix = config.bot.prefix)

# Basic admin commands to load modules
@client.command()
@commands.has_role("Admin")
async def load (ctx, extension):
    """Load bot modules"""
    await ctx.send(f"Loading {extension}")
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_role("Admin")
async def unload (ctx, extension):
    """Unload bot modules"""
    await ctx.send(f"Unloading {extension}")
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_role("Admin")
async def reload (ctx, extension):
    """Reload bot modules"""
    await ctx.send(f"Reloading {extension}")
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# Load all found cogs
logs.logging.info("Loading cogs")
for i in os.listdir("./cogs"):
    if i.endswith(".py"):
        client.load_extension(f'cogs.{i[:-3]}')

client.run(config.bot.token)
