import discord
from discord.ext import commands

class Moderation(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(ctx, member : discord.member):
        await ctx.send("WIP COMMAND")

    @commands.command()
    async def ban(ctx, member : discord.member):
        await ctx.send("WIP COMMAND")
    
    @commands.command()
    async def mute(ctx, member : discord.member, time):
        await ctx.send("WIP COMMAND")

async def setup(bot):
    await bot.add_cog(Moderation(bot))