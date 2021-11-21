# インストールした discord.py を読み込む
import discord, os

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # 変数を定義
    NEKO="/neko"
    HELP="/help_yukuto"

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == NEKO:
        await message.channel.send('にゃーん')

    # /help_yukuto | 要件をどうぞ
    if message.content == HELP:
        await message.channel.send \
                ('####要件をどうぞ####\n'\
                 '1：yukutoの自己紹介\n'\
                 '2：snakeの自己紹介')


# Botの起動とDiscordサーバーへの接続
client.run(os.environ["TOKEN"])
