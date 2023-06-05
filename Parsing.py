from bs4 import BeautifulSoup
import requests
import csv
import time
from random import randint

file = open('chita.csv', 'w', newline= '', encoding='utf-8')
csv_w = csv.writer(file)
csv_w.writerow(['Product Title', 'Price'])

for i in range(1,6):
    pg = i
    url = f'https://chita.ge/en/shop-2/page/{pg}/'
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_soup = soup.findAll('li', class_ = 'jet-woo-thumb-with-effect' )

    for product in product_soup:
        title = product.find('h2', class_ = 'woocommerce-loop-product__title').find('a').text
        price = product.find('bdi').text[:-2]
        # print(title)
        # print(price)
        csv_w.writerow([title,price])

    time.sleep(randint(15,20))
file.close()




