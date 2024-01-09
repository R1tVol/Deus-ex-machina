import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTE5MTgwODExMDAyMTU4NzAwNQ.GSMWqt.AXIn5O_VRcE7TwH3C8ppoeAGE13Fq2MCCeNE8I")
