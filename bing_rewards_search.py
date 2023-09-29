# source: https://stackoverflow.com/questions/18834636/random-word-generator-python 
from urllib.request import urlopen
import random
import webbrowser
import re
  

#forbidden_words=["fu","shi","bit","as","por","pus","nu","ti","cu","bu","bb","vi","pen","va","cli","co","se","boo","bre","ora","hen","nak","lab","ji","di","ana","br","sl","dru","mas","wan","les","ho","linge","hand","inc","ama","blo","three","miss","vo","test","spe","ni","bab","gir","squ","ns","liv","bon","ori","rom","dy","play","bj","hj","lol","mur","fac","lai"]

with open("D:\\DocumentsD\\Programming\Python\\bing_rewards\\forbidden_words.txt") as file:
    forbidden_words = [line.rstrip() for line in file]

def is_forbidden(word: str):
    for forbidden_word in forbidden_words:
        match = re.search(forbidden_word, word)
        if match:
            return True
    return False

# match = re.search(r'portal', 'GeeksforGeeks: A computer science \
#                   portal for geeks')
# print(match)
# print(match.group())
  
# print('Start Index:', match.start())
# print('End Index:', match.end())

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

# with open("newline.txt", "r") as file: 

# crimefile = open(fileName, 'r')
# yourResult = [line.split(',') for line in crimefile.readlines()]

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

