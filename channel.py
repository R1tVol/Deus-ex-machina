import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command(name='eklekanal', help='Kanal ekle. Kullanım: !eklekanal kanal_adı')
async def eklekanal(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await ctx.send(f"Kanal oluşturuldu: {channel_name}")
    else:
        await ctx.send("Bu isimde bir kanal zaten var!")

@client.command(name='silkanal', help='Kanal sil. Kullanım: !silkanal kanal_adı')
async def silkanal(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if existing_channel:
        await existing_channel.delete()
        await ctx.send(f"Kanal silindi: {channel_name}")
    else:
        await ctx.send("Bu isimde bir kanal bulunamadı!")

client.run("Enter ur token")
