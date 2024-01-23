import discord
import random
from discord.ext import commands

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

bot = commands.Bot(command_prefix='$')


memes = {
    'animals': ['animal1.png', 'animal2.png'],
    'programming': ['code1.png', 'code2.png']
}

@bot.command()
async def meme(ctx, category=''):
    if category.lower() in memes:
        meme_list = memes[category.lower()]
        meme_name = random.choice(meme_list)
        with open(f'images/{meme_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("Belirtilen kategori bulunamadı.")


client.run("You do not have permission to view tokens, paste your own token")
