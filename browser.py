import requests
from bs4 import BeautifulSoup


class Browser:
    def __init__(self, address):
        self.address = address

    def get_page(self):
        url = f'https://{address}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup.text)


while True:
    address = input()
    if address == 'exit':
        break
    else:
        page = Browser(address)
        page.get_page()
