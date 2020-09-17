import os
import random
from nltk.chat.util import Chat, reflections
from discord.ext import commands
from dotenv import load_dotenv
from dialogue import pairs
from benderClass import bender

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
used_quotes = []
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
        used = True
        count = 0

        ## Check is quote has already been used previously in the past 3 iterations
        while used is True:
            quote = response.respond(M)
            if quote is None:
                quote = random.choice(bender().rand_quote)

            if quote not in used_quotes:
                used = False
                continue

            else:
                count += 1
                if count > 10:
                    used = False
                    continue

        used_quotes.append(quote)
        if len(used_quotes) > 2:
            print(used_quotes)
            del used_quotes[0]

        await message.channel.send(quote)
bot.run(TOKEN)