import discord

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
    msg = message.author.mention + " Hi."
    await message.channel.send("お呼びかな？")

client.run("OTEwMTQyNTkwOTMyODkzNzU2.YZOiVw.tMI1qZ2fw0mHrdbg7LoTaZg_yD8")
