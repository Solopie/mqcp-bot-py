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

@bot.command(name="timer", help=f"Creates a timer: {PREFIX}timer <minutes> [title]")
async def timer(ctx, minutes:int, title="Timer"):
    if minutes <= 0 or minutes > 30:
        raise commands.errors.BadArgument
        
    timer = Timer(ctx, int(minutes), title)

    await timer.start_timer()

@timer.error
async def timer_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.reply("\"minutes\" is a required argument that is missing.")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.reply("\"minutes\" argument must be a number between 1 and 30.")



bot.run(TOKEN)

