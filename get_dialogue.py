from imdsb_scrape import data_scrape
from parse_screenplay import parse_dialogues
from pprint import PrettyPrinter
from collections import defaultdict
from tqdm import tqdm
import yaml

if __name__ == "__main__":
    # Get links
    print('Getting links')
    links = data_scrape('https://www.imsdb.com/TV/Futurama.html', 'Futurama')

    # Parse dialogues
    all_dialogues = []
    for link in tqdm(links, desc='Parsing dialogues'):
        dialogues = parse_dialogues(link)
        all_dialogues.append({
            'link': link,
            'dialogues': dialogues
        })
    
    # Write to file
    print('Writing to file...')
    with open('dialogues.yaml', 'w+') as f:
        yaml.dump(all_dialogues, f)