import os
import nextcord
from nextcord.ext import commands
import pytz
import os
from flask import Flask
from threading import Thread
import asyncio


app = Flask("")


@app.route("/")
def index():
    return "<h1>Bot is running</h1>"


Thread(target=app.run, args=("0.0.0.0", 8080)).start()

bot = commands.Bot(command_prefix='+')
bot.remove_command('help')
client = nextcord.Client

@bot.event
async def on_ready():
    await bot.change_presence(
        status=nextcord.Status.idle,
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching,
            name='Techniq Bot Company')
    )
    print('Airbus_bot is up and ready to serve!')

@bot.command()
async def assemble(ctx,serial,type_air):

	if type_air == "shorthaul":
		assem_time = 12*3600
		message = await ctx.send("Starting Assembly")
	elif type_air == "mediumhaul":
		assem_time = 24*3600
		message = await ctx.send("Starting Assembly")
	elif type_air == "longhaul":
		assem_time = 36*3600
		message = await ctx.send("Starting Assembly")
	else:
		await ctx.send("Invalid")
	while True:
		await asyncio.sleep(5)
		assem_time -= 5
		if assem_time >= 3600:
				await message.edit(content=f"Assembly ends in {assem_time//3600} hours {assem_time %3600//60} minutes {assem_time%60} seconds")
		elif assem_time >= 60:
				await message.edit(content=f"Assembly ends in  {assem_time//60} minutes {assem_time%60} seconds")
		elif assem_time < 60:
				await message.edit(content=f"Assembly ends in {assem_time} seconds")
		
		
		if assem_time <= 0:
				await message.edit(content="Ended!")
				await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")


@bot.command()
async def help(ctx):
	embed = nextcord.Embed(title = "Help",
	color = 0x04235b
	)
	embed.add_field(name = "+assemble <serial_no> <shorthaul/mediumhaul/longhaul>", value = "Timer for Assembly")

	await ctx.send(embed=embed)

	

bot.run('token') # replace token with your bot's token
