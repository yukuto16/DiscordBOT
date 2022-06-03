import pickle
import discord
import os
from sample.python import bot_config

client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # dumpファイル作成i
    PF = [bot_config.HELP_RESUL, bot_config.USER_ID]
    with open('temp.binaryfile', 'wb') as BF:
        pickle.dump(PF, BF)
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # dumpファイル読み込み
    with open('temp.binaryfile', 'rb') as BF:
        PF = pickle.load(BF)

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == bot_config.NEKO:
        await message.channel.send('にゃーん')

    # /help_yukuto | 要件をどうぞ
    if message.content == bot_config.HELP:
        HELP_RESULT = 1
        USER_ID = message.author
        print(USER_ID)
        msg = await message.channel.send \
            ('####要件をどうぞ####\n' \
             'Ⅰ：アラームの設定\n' \
             # TODO
             # Ⅱ：自動切断設定\n' \
             'Ⅲ：なんでもない')
        await msg.add_reaction(bot_config.REACTION_1)
        # TODO
        # await msg.add_reaction("bot_config.REACTION_2")
        await msg.add_reaction(bot_config.REACTION_3)

        msg_id = msg.id

    # /help_yukuto -> Ⅰ
    # ネスト構造
    # TODO
    # リアクションされた時点で呼び出される？
    # トリガーとなるリアクションを設定できない？
    async def on_raw_reaction_add(res):
        if res.message_id == msg_id:

            # TODO
            # アラーム処理の関数を呼び出す


        # dumpファイル保存
        PF = [HELP_RESULT, USER_ID]
        with open('temp.binaryfile', 'wb') as BF:
            pickle.dump(PF, BF)


# await message.channel.send \
# ('####アラームを設定しますか？####')

# 書き出し処理
joblib.dump(bot_config)

# Botの起動とDiscordサーバーへの接続
client.run(os.environ["TOKEN"])
