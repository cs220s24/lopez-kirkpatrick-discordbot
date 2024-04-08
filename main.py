# import discord.py
import discord

#import the os module

import os

#import load dotenv function from dotenv module
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# gets the client object from discord.py
bot = discord.Client()

#Event listener for whemn the bot has been switched from offline to online
@bot.event
async def on_ready():
	#creates a counter for how many servers the bot is in
	guild_count = 0
	
	
	#loops through all the servers
	for guild in bot.guilds:
		#print the servers id and name
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("Bot is in " + str(guild_count) + " servers.")


@bot.event
async def on_message(message):
	#checks if the message that was sent is equal to "HELLO"
	if message.content == "hello":
	
		#sends back a message to the channel
		await message.channel.send("YOOOOOOO")

# EXECUTE THE BOT
bot.run(DISCORD_TOKEN)
