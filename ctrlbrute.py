#!/usr/bin/env python
from Color_Console import *
import os 
import ctypes
import easygui
import random
import string
import requests
import socket
from bs4 import BeautifulSoup
import subprocess
import urllib.request
import sys 
from datetime import datetime
import re
from threading import Thread

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

#Colors
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

hits = 0
bad = 0
lin = 0
inf = 1
er = 0

def main_menu():
    os.system("cls")
 
    print("\u001b[36m  ______________  __   ___  ___  __  ____________")
    print(" / ___/_  __/ _ \/ /  / _ )/ _ \/ / / /_  __/ __/")
    print("/ /__  / / / , _/ /__/ _  / , _/ /_/ / / / / _/  ")
    print("\___/ /_/ /_/|_/____/____/_/|_|\____/ /_/ /___/ v1 ")
    print("\u001b[32m             Ctrlv.cz Bruteforcer \u001b[37m")
    print("-" * 50)


    base_url = 'https://ctrlv.cz/{}'

    show_invalid = input("\nDo you want to show invalid links in output?[y/n]: ")
    print("")

    found_ss = []

    def download_image(base_url: str):
        page_data = requests.get(url=base_url).text
        idk = re.search('(?<=<img src=").*(?=" class="outline")', page_data).group(0)
        direct_url = f'https://ctrlv.cz{idk}'

        file_name = base_url.replace('https://ctrlv.cz/', '')
        if not os.path.isfile("images/{file_name}"):
            content = requests.get(url=direct_url).content
            open(f'images/{file_name}.png', 'wb').write(content)
        else:
            already_exist += 1

    def create_path():
        if not os.path.exists('images'):
            os.mkdir('images')
        else:
            print("\u001b[33;1m[!]\u001b[37m Images folder already exist")
            print("")
  
    def random_char(y: int):
        return ''.join(random.choice(string.ascii_letters + "0123456789") for x in range(y))

    def update_title(hits: int, bad: int):
        ctypes.windll.kernel32.SetConsoleTitleW(f'CTRLBRUTE | Hits: {hits} | Bads: {bad} | Soudruh Danny | https://discord.gg/gdKApcS')


    def worker():
        global hits 
        global bad
        while True:
            try:
                random_string = random_char(4)
                if not found_ss.__contains__(random_string):
                    response = requests.get(url=base_url.format(random_string)).text
                    if not response.__contains__('notexists.png'):
                        print(f'\u001b[32m[VALID] {base_url.format(random_string)}\u001b[37m')
                        hits += 1
                        download_image(base_url.format(random_string))
                        update_title(hits, bad)
                    else:
                        if show_invalid == "y":
                            print(f'\u001b[31;1m[INVALID] {base_url.format(random_string)}\u001b[37m')
                            bad += 1
                            update_title(hits, bad)
                        else:
                            bad += 1
                            update_title(hits, bad)
                else:
                    print(f'\u001b[33;1m[DUPLICATE]  {base_url.format(random_string)}\u001b[37m')
            except:    
                time.sleep(3)
                worker()

    if __name__ == "__main__":
        create_path()
        update_title(hits, bad)
        threadnum = int(input("Threads: "))

        c = 0
        while c < threadnum:
            processThread = Thread(target=worker)
            processThread.start()
            c += 1
main_menu()
