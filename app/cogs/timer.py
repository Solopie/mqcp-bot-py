from discord.ext import tasks, commands
from discord import Embed, Colour

class Timer():
    def __init__(self, ctx, mins, title):
        self.ctx = ctx
        self.mins = mins
        self.title = title
        self.msg = None

    async def start_timer(self):
        new_embed = Embed(title=self.title, description=f"{self.mins} min(s)", colour=Colour.red())
        self.msg = await self.ctx.send(embed=new_embed)
        self.update_time.start()

    def stop_timer(self):
        self.update_time.cancel()

    
    @tasks.loop(seconds=60.0)
    async def update_time(self):
        if self.mins == 0:
            self.stop_timer()
            return
        
        new_embed = Embed(title=self.title, description=f"{self.mins} min(s)", colour=Colour.red())
        await self.msg.edit(embed=new_embed)

        self.mins -= 1

    @update_time.after_loop
    async def timer_completed(self):
        new_embed = Embed(title="Timer", description="Done!", colour=Colour.green())
        await self.msg.edit(embed=new_embed)
        await self.ctx.reply(f"Timer \"{self.title}\" is done")