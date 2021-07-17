import discord
from discord.ext import commands
import asyncio
import os
bot = commands.Bot(command_prefix = '!')


@bot.command(pass_context = True)
async def ping(ctx):
     role = ctx.guild.get_role(863103946063478824) 
     await ctx.author.add_roles(role, reason=None)
     await asyncio.sleep(7200)
     await ctx.author.remove_roles(role, reason=None)

token = os.environ.get("BOT_TOKEN")
bot.run(str(token))




