import discord
from discord.ext import commands, tasks
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

with open("token.txt") as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix="!")


def Translate(message):
    try:
        translated = translator.translate(message, dest="en")
        return translated.text
    except Exception as e:
        print(e)
        return "Error"


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def translate(ctx, arg):
  await ctx.send(Translate(arg))

client.run(TOKEN)
