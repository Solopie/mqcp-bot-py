from discord.ext import commands
from util.config import TOKEN, PREFIX

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)

