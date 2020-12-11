import discord
from utils import config, api
from utils.logs import logging
import asyncio
import aiohttp
from discord.ext import tasks,commands
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
            await ctx.send(f"{signal}ing server".replace("stop","stopp").capitalize())
            await api.sendSignal(signal)
        else:
            await ctx.send("Invalid power signal")

    @tasks.loop(minutes=2)
    async def checkServerStatus(self):
        status = await api.getStatus()
        attributes = status["attributes"]
        if attributes['memory']['current'] > attributes['memory']['limit']:
            logging.warn(f"Detected memory problem, {attributes['memory']['current']}/{attributes['memory']['limit']}, killing and restarting server")
            await self.client.get_channel(int(config.discord.modLogsChannel)).send(f"Detected memory problem, {attributes['memory']['current']}/{attributes['memory']['limit']}, killing and restarting server")
            await api.sendSignal("kill")
            await api.sendSignal("start")


    @commands.command() 
    @docstring_parameter(config.bot.prefix) 
    async def status(self, ctx):
        """
        Usage: {0}status
        
        Get the current status of the server
        """
        status = await api.getStatus()
        attributes = status["attributes"]
        message = f"Current server status:\n> State: {attributes['state']}\n> Current CPU Usage: {attributes['cpu']['current']}%/{attributes['cpu']['limit']}%\n> Memory Usage: {attributes['memory']['current']}/{attributes['memory']['limit']}\n> Disk Usage: {attributes['disk']['current']}/{attributes['disk']['limit']}"
        await ctx.send(message)
    
def setup(client):
    client.add_cog(Server(client))