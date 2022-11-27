import pickle
import discord
import os
import bot_config
from discord.ext import tasks
from datetime import datetime

client = discord.Client(intents=discord.Intents.all())


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# タイマー処理
@tasks.loop(seconds=60)
async def loop(sec,channel_id):
    # 現在の時刻
    NOW = datetime.now().strftime('%H:%M')
    if NOW == sec:
        channel = client.get_channel(channel_id)
        await channel.send('おはよう')  
        pass


# メッセージ受信時に動作する処理
@client.event
async def on_message(message, time = ""):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == bot_config.NEKO:
        await message.channel.send('にゃーん')

    # タイマー設定
    if message.content == bot_config.TIME:
        CHANNEL_ID = message.channel
        loop.start(time, CHANNEL_ID)

    # /help_yukuto | 要件をどうぞ
    if message.content == bot_config.HELP:
        await message.channel.send \
            ('####コマンド一覧####\n' \
             '/time xx:xx | アラームの設定\n' \
             '/neko | 鳴き声\n')

# Botの起動とDiscordサーバーへの接続
client.run(os.environ["TOKEN"])
