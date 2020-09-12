import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    brooklyn_99_quotes = [
    'I\'m the human form of the 💯 emoji.',
    'Bingpot!',
    (
        'Cool. Cool cool cool cool cool cool cool, '
        'no doubt no doubt no doubt no doubt.'
    ),
    'Dammit Andy, I need you to update the tfbender bot so I can start pulling quotes',
    'Oh crap! My asss is on fire', 
    'Andy if you keep spamming this, this is really cool, simple, but it''s also super complicated', 
    'Really though Andy, update them quotes!'
    ]
    almond_quotes = ['Hello, you have reached an automated message reply.', 
    'Bite my shiny metal ass', 
    'Why are there so many group chats', 
    'You guys message so much that I can''t keep up with it so I created a bot to help me with the conversation', 
    'God damn, there is just way to much to mention',
    'Stop harassing me!', 
    'Fine, fuck off watch this: https://www.youtube.com/watch?v=oHg5SJYRHA0' 
    ]
    if bot.user.mentioned_in(message):
        
        M = message.content
        print(type(M))
        if "Hello" in M:
            response = "Yo whatsup my homie"
        elif "Raymond told me to message you" in M:
            response = random.choice(almond_quotes)
        elif "Wow" in M:
            response = "Stop it"
        else:
            response = random.choice(brooklyn_99_quotes)
            
        await message.channel.send(response)
    
bot.run(TOKEN)