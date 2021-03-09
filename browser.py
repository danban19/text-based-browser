import requests
import sys
import os
from colorama import Fore, init
from collections import deque
from bs4 import BeautifulSoup
init(autoreset=True)


class Browser:
    def __init__(self, directory, address, history):
        self.directory = directory
        self.address = address
        self.history = history

    def create_dir(self):  # creates a directory for webpages
        try:
            os.mkdir(self.directory)
        except FileExistsError:
            pass
        os.chdir(self.directory)
        file_name = self.address.replace('.com', '.txt')
        with open(f'{file_name}', 'a', encoding='utf-8') as self.file:  # opens a file for a specific url
            self.get_page()
        os.chdir('..')

    def get_page(self):  # creates an url and extracts text from it
        url = f'https://{self.address}'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                     "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        try:
            r = requests.get(url, headers={'User-Agent': user_agent})
        except requests.exceptions.ConnectionError:
            print('Error: Incorrect URL')
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            text = '\n'.join([p.text.strip() for p in soup.find_all(('p', 'script', 'div'))])
            print(Fore.BLUE + text)
            print(Fore.BLUE + text, file=self.file)
            self.history.append(Fore.BLUE + text)


history = deque()
directory = sys.argv[1]  # arguments from the command line

while True:
    address = input()
    if address == 'exit':
        break
    elif address == 'back':
        try:
            history.pop()
            print(history.pop())
        except IndexError:
            pass
        else:
            continue
    try:
        if '.' not in address:
            raise ConnectionError
    except ConnectionError:
        print('Error: Incorrect URL')
        continue
    else:  # enters the class if the arguments are valid
        page = Browser(dir, address, history)
        page.create_dir()
