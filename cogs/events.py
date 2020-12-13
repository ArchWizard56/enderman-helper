import aiohttp
import discord
import re
import traceback
from utils import config,api
from utils.logs import logging
from discord.ext import commands, tasks



class Events(commands.Cog):
    def __init__ (self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have the permissions to run this command")
            return

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"I couldn't find that command, try {config.bot.prefix}help")
            return
        
        print('Something went wrong!')
        logging.warning(traceback.format_exc())

    @commands.Cog.listener()
    async def on_ready(self):
       await self.client.change_presence(activity=discord.Game(config.bot.status))
       logging.info("The bot becomes ready")

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if int(message.channel.id) == int(config.discord.chatChannel) and not message.author.bot:
            command = f'tellraw @a ["",{{"text":"[DISCORD]","color":"light_purple"}},{{"text":" <{message.author}> {message.content}"}}]'
            await api.sendCommand(command)

        if int(message.channel.id) == int(config.discord.consoleChannel):
            m = re.search(r'\[\d*:\d*:\d*\] \[Async Chat Thread - #\d*\/INFO\] <(.*)> (.*)',message.content)
            if m != None:
                await self.client.get_channel(int(config.discord.chatChannel)).send(f"[MINECRAFT] <{m.group(1)}> {m.group(2)}")
                return

            j = re.search(r'\[\d*:\d*:\d*\] \[Server thread\/INFO] (.*) joined the game',message.content)
            if j != None:
                await self.client.get_channel(int(config.discord.chatChannel)).send(f"[MINECRAFT] {j.group(1)} joined the game")
                return

            l = re.search(r'\[\d*:\d*:\d*\] \[Server thread\/INFO] (.*) left the game',message.content)
            if l != None:
                await self.client.get_channel(int(config.discord.chatChannel)).send(f"[MINECRAFT] {l.group(1)} left the game")
                return


def setup(client):
    client.add_cog(Events(client))