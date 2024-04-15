# source: https://stackoverflow.com/questions/18834636/random-word-generator-python 
from urllib.request import urlopen
from argparse import ArgumentParser
import random
import webbrowser
import re
import time
  

parser = ArgumentParser()
parser.add_argument("-s", "--number", help="number of searches", type=int, default=31)
parser.add_argument("-t", "--time", help="seconds between searches", type=int, default=329)
args = parser.parse_args()
num_searches = args.number
time_between = args.time


with open("D:\\DocumentsD\\Programming\\Python\\bing_rewards\\forbidden_words.txt") as file:
    forbidden_words = [line.rstrip() for line in file]


def is_forbidden(word: str):
    for forbidden_word in forbidden_words:
        match = re.search(forbidden_word, word)
        if match:
            return True
    return False


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urlopen(word_site)
txt = response.read()
words = txt.splitlines()
search_words = []

for i in range(num_searches):
    should_stop = False
    while True:
        random_word = bytes.decode(words[random.randrange(0,9999,1)])
        if not is_forbidden(random_word) and random_word not in search_words:
            print(f'Search {random_word}?')
            response = input()
            if response == 'y':
                break
            elif response == 'exit' or response == 'q':
                should_stop = True
                break
            else:
                with open("D:\\DocumentsD\\Programming\\Python\\bing_rewards\\forbidden_words.txt", 'a') as file:
                    file.write(random_word + "\n")
    if should_stop:
        break
    search_words.append(random_word)
    print(f'{i+1}) Added {random_word}')

url_prefixes = ['search?PC=U523&q=', 'search?FORM=U523DF&PC=U523&q=', 'search?q=']
url_suffixes = ['&FORM=ANAB01', '', '']

j = 1
for search_word in search_words:
    print(f'{j}) Searching {search_word}')
    url_index = random.randrange(0,len(url_prefixes),1)
    webbrowser.open(f'https://www.bing.com/search?q={search_word}', new=1)
    time.sleep(time_between + random.randrange(0,13,1))
    j += 1
