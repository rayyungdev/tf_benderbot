import os
import random
from nltk.chat.util import Chat, reflections
from discord.ext import commands
from dotenv import load_dotenv
from dialogue import pairs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):

    if bot.user.mentioned_in(message):
        
        M = message.content
        M = ' '.join(M.split()[1:])
        M = M.lower()
        response = Chat(pairs, reflections)
        try:
            await message.channel.send(response.respond(M))
        except:
            await message.channel.send("What did you say? Something went wrong")
        
    
bot.run(TOKEN)