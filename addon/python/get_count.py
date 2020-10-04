from bs4 import BeautifulSoup
import requests
import sys

def getCount(page, word):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.get_text().count(word)

if __name__ == "__main__":
    getCount(sys.argv[0], sys.argv[1])
        