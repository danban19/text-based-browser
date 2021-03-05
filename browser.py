import requests
import sys
import os
from bs4 import BeautifulSoup


class Browser:
    def __init__(self, dir, address):
        self.dir = dir
        self.address = address

    def create_dir(self):
        try:
            os.mkdir(self.dir)
        except FileExistsError:
            pass
        os.chdir(self.dir)
        file_name = address.replace('.com', '')
        self.file = open(f'{file_name}', 'a', encoding='utf-8')
        self.get_page()
        self.file.close()
        os.chdir('..')

    def get_page(self):
        url = f'https://{address}'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        try:
            r = requests.get(url, headers={'User-Agent': user_agent})
        except requests.exceptions.ConnectionError:
            print('Error: Incorrect URL')
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            print(soup.text)
            print(soup.text, file=self.file)


dir = sys.argv[1]

while True:
    address = input()
    if address == 'exit':
        break
    try:
        if not '.' in address:
            raise ConnectionError
    except ConnectionError:
        print('Error: Incorrect URL')
        continue
    else:
        page = Browser(dir, address)
        page.create_dir()
