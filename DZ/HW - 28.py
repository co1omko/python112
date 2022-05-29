import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def refine_price(s):
    return s.split()[:2]


def write_csv(data):
    with open('pluginsHW.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['name'],
                         data['url'],
                         data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    elements = soup.find_all('div', class_='catalog-card')
    for el in elements:
        try:
            name = el.find('a', class_='catalog-card__title cart-modal-title').text
        except ValueError:
            name = ''

        try:
            url = el.find('a').get('href')
        except ValueError:
            url = ''

        try:
            price = el.find('div', class_='catalog-card__price-row').find('a',
                                                                          class_='catalog-card__price').text.strip()
            pr = refine_price(price)
        except ValueError:
            pr = ''

        data = {
            'name': name,
            'url': url,
            'price': pr
        }

        write_csv(data)


def main():
    url = 'https://biggeek.ru/catalog/apple-iphone'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
