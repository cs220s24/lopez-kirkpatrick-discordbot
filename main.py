import discord
from discord.ext  import commands
from discord.ext.commands import Bot
import redis
import random
#import the os module

import os

#import load dotenv function from dotenv module
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


if port is None:
    port = 6379
    
if host is None:
    host = 'localhost'

#start the redis server if it is not already running
os.system('redis-server --daemonize yes')

#connect to the redis server

r = redis.Redis(host=host, port=port)

def get_num_jokes():
    num_jokes = r.get('num_jokes')
    if num_jokes == None:
        return 0
    else:
        return int(num_jokes)

def get_joke():
    num_jokes = get_num_jokes()
    if num_jokes == 0:
        return "Why did the chicken cross the road? To get to the other side!"
    else:
        joke = r.get(f'joke{int(random.random()*num_jokes)}')
        return str(joke)[2:-1]
    
def get_joke_n(n):

    if int(n) + 1 > get_num_jokes() or int(n) < 0:
       return "Joke not found!"

    else: 
       joke = r.get(f'joke{n}')
       return str(joke)[2:-1]
   
        

def append_joke(joke):
    if get_num_jokes() == 0:
        r.set('num_jokes', 0)
    num_jokes = get_num_jokes()
    r.set(f'joke{num_jokes}', joke)
    r.set('num_jokes', int(num_jokes) + 1)
    return "Joke added!"

# gets the client object from discord.py
bot = discord.Client(intents=discord.Intents.all())

#Event listener for when the bot has been switched from offline to online
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


#Event listener for when the bot has received a message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send('YOOOOOOO')
        
    if '!joke' in message.content:
        await message.channel.send(get_joke())
        
    if '!addjoke ' in message.content:
        affirmation = append_joke(message.content.removeprefix('!addjoke '))
        await message.channel.send(affirmation)

    if '!getjoke ' in message.content:
         try:
            jokenumber = int(message.content.removeprefix('!getjoke ')) - 1
            await message.channel.send(get_joke_n(jokenumber))
         except:
            await message.channel.send("That's not a number!")




# EXECUTE THE BOT
bot.run(DISCORD_TOKEN)
