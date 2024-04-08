import discord
from discord.ext import commands
print("Creditos: yfrusted e 1um2")
token = input("Token do bot:")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.run(token)
