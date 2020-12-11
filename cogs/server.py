import discord
from utils import config, api
import asyncio
import aiohttp
from discord.ext import commands
import websockets
import json

def docstring_parameter(*sub):
     def dec(obj):
         obj.__doc__ = obj.__doc__.format(*sub)
         return obj
     return dec

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @docstring_parameter(config.bot.prefix)
    async def mc (self, ctx, *, chat):
        """
        Usage: {0}mc message

        Send a message to the minecraft server chat
        """
        command = f'tellraw @a ["",{{"text":"[DISCORD]","color":"light_purple"}},{{"text":" <{ctx.author}> {chat}"}}]'
        await api.sendCommand(command)

    @commands.command()
    @docstring_parameter(config.bot.prefix)
    async def server(self, ctx, *, signal):
        """
        Usage: {0}server <kill | stop | start | restart>
        
        Send a power signal to the server
        """
        if signal in ["kill", "stop", "start", "restart"]:
            await ctx.send(f"{signal}ing server".capitalize())
            await api.sendSignal(signal)
        else:
            await ctx.send("Invalid power signal")
    
def setup(client):
    client.add_cog(Server(client))