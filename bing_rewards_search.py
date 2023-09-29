# source: https://stackoverflow.com/questions/18834636/random-word-generator-python 
from urllib.request import urlopen
import random
import webbrowser
import re
  

with open("D:\\DocumentsD\\Programming\Python\\bing_rewards\\forbidden_words.txt") as file:
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

for i in range(33):
    should_stop = False
    while True:
        random_word = bytes.decode(words[random.randrange(0,9999,1)])
        if not is_forbidden(random_word):
            print(f'Search {random_word}?')
            response = input()
            if response == 'y':
                break
            elif response == 'exit':
                should_stop = True
                break
            else:
                with open("D:\\DocumentsD\\Programming\Python\\bing_rewards\\forbidden_words.txt", 'a') as file:
                    file.write(random_word + "\n")
    if should_stop:
        break
    webbrowser.open(f'https://www.bing.com/search?q={random_word}', new=1)
    print(f'{i+1}) Searching {random_word}')

