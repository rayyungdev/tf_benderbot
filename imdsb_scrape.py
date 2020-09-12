import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import pandas as pd
import numpy as np


# # This code is meant to import screenplays from imsdb.com (Futurama) and automatically import all of them for preprocessing. 
# 
# I've tested the current function and this works with separating names from characters for two scripts.


def data_scrape(link, sname):
    page = requests.get(link) #Go to IMSDB link
    soup = BeautifulSoup(page.content, features="lxml") #Pull the content
    links = soup.find_all('a') #Pull links
    titles = [] 
    for title in links:
        temp = title.get('title') #only pull links with the word title in them
        if (temp is not None) and ('Script' in temp): #Only Pull values that are not none and with the words script in them
            if temp not in titles:
                titles.append(temp)
    titles=titles[1:-1] #ignore the first and last lines
    nlink=[] 
    for index in range(len(titles)):
        titles[index]=titles[index].split('Script')[0]
        nlink.append(titles[index])
        nlink[index]=nlink[index].replace(" ","-")
        nlink[index]=nlink[index].strip("-")
        nlink[index]="https://www.imsdb.com/transcripts/"+sname+'-'+nlink[index]+".html"
    return np.asarray(nlink), np.asarray(titles)


# In[3]:


def gscrnplay(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, features="lxml")
    text = soup.find('td', class_= 'scrtext').get_text()
    text = text.split('THE END')[0] #We don't need anything below 'THE END'
    temp=text.split('\n\n') #Separates the Title Sequence since it's unneeded. 
    ### Need to fix this so that it's automated. Sectioned 8 might not be used for all TV scripts
    scrnplay = ''.join(temp[8:]) #Connect the strings back together, except the title sequence
    return scrnplay

def gcharnames(scrnplay):
    characters = scrnplay.split(' \n') #Remove lines that have issues
    #names is a list of the characters in the dialogue.
    names = []; #Create empty list
    for test in characters:
        scr = test.split('\n') #Separate more lines
        if len(scr) > 1:
            pname=(scr[0].strip()).split('\n') #Remove spaces and the more lines to separate the character names from dialogue
            for n in pname:
                if n.isupper() is True: #Characters are separated from dialogue via uppercase.
                    n= n.split('[')
                    n = n[0]
                    n = ''.join(u for u in n if u not in ("."))
                    n = n.strip()
                    n = n.strip('"')
                    if n not in names:
                        names.append(n)
    return names

titles = data_scrape('https://www.imsdb.com/TV/Futurama.html', 'Futurama')

data = [];
for i,j in zip(titles[0], titles[1]):
    info = {};
    scrnplay = gscrnplay(i)
    data.append({
        "title" : j,
        "scrnplay" : scrnplay,
        "characters" : gcharnames(scrnplay) 
    })

script = data[0]['scrnplay']
test = script.split('\n');
for i in range(len(test)):
    test[i] = test[i].strip();
test_list = [i for i in test if i]