from discord.ext import commands

import discord

import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Nerd bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Nerd Bot is running")

@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    if (message.channel.id != CHANNEL_ID):
        return
    if (message.author.id == 1049363045987663964):
        return
    
    await message.channel.send(f"\"{message.content}\" 🤓")
    emoji = '\N{Nerd Face}'
    await message.add_reaction(emoji)
    
    

bot.run(BOT_TOKEN)