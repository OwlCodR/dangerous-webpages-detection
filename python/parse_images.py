from bs4 import BeautifulSoup
import requests

# This file searches images in Yandex.Images

search_words = str(input('Запрос: ')).split()
url = 'https://yandex.ru/images/search?text='
for word in search_words:
    if word != search_words[0]:
        url += '%20'
    url += word

soup = BeautifulSoup(requests.get(url).text, 'html')
print(soup.findAll('a', class_='lenta'))
