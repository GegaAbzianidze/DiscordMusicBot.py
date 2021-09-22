import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='!',
intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODkwMjQxNDQ5MzY5Njg2MDY2.YUs79Q.c3dudwuCY_TIzGyPbnFFabh6ONU")

