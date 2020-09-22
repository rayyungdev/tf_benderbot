import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import pandas as pd
import numpy as np
from pprint import PrettyPrinter
import re
from collections import defaultdict

def parse_dialogues(link):
    # Get link and make dat soop
    page = requests.get(link) # Go to IMSDB link
    soup = BeautifulSoup(page.content, features="lxml") # Pull the content
    text = soup.find('td', class_='scrtext').get_text() # Get text

    # Split into lines
    lines = re.split(r'\n+', text)
    lines = [
        '' if re.match('^\s+$', line) else line
        for line in lines
    ]

    # Start after title
    lines = lines[8:]

    # Start line iterator
    lineiter = iter(lines)

    character_regex = re.compile('^\s+([A-Z]+)$')
    dialogues = []

    # Line iterator will throw us a StopIteration error when we run out of lines
    try:
        while True:
            # Find first instance of character
            line = next(lineiter)
            match = character_regex.match(line)
            while not match:
                line = next(lineiter)
                match = character_regex.match(line)
            character = match.group(1)

            # Now find every line until an empty line
            dialogue = []
            line = next(lineiter)
            while line != '':
                dialogue.append(line)
                line = next(lineiter)
            dialogue = [ line.strip() for line in dialogue ]
            dialogue = [ line.rstrip() for line in dialogue ]
            dialogue = ' '.join(dialogue)

            # Append to dialogues
            dialogues.append({
                'character': character,
                'dialogue': dialogue
            })
        
    except StopIteration:
        pass

    return dialogues