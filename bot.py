import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')


class Client(discord.Client):
    @bot.event
    async def on_ready(self):
        print('Logged on as', self.user)

    @bot.command()
    async def neko(ctx):
        await ctx.send('にゃーん')

    @bot.command()
    async def help(ctx):
        await ctx.send('###用件をどうぞ###\n 1:アラームの設定\n 2:自動切断設定\n 3:なんでもない')


client = Client()
client.run(os.environ["TOKEN"])
