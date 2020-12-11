import discord
from utils import config
import asyncio
from discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def sayhello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")
    
    @commands.command()
    async def connect(self, ctx):
        if config.server.port != "25565":
            await ctx.send(f"To connect to the server use `{config.server.host}:{config.server.port}`")
        else:
            await ctx.send(f"To connect to the server use `{config.server.host}`")

def setup(client):
    client.add_cog(Info(client))