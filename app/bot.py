from discord.ext import commands
from discord import Embed
from util.config import TOKEN, PREFIX
from cogs.timer import Timer

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="ping", help=f"Test command: {PREFIX}ping")
async def ping(ctx):
    await ctx.send("pong")

@bot.command(name="timer", help=f"Creates a timer: {PREFIX}timer <number minutes> [title]")
async def timer(ctx, mins, title="Timer"):
    try:
        mins = int(mins)
    except:
        return await ctx.reply("Invalid number")

    if mins <= 0 or mins > 30:
        return await ctx.send("Please keep minutes between 1 - 30")
        
    timer = Timer(ctx, int(mins), title)

    await timer.start_timer()

bot.run(TOKEN)

