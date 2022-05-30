# from bs4 import BeautifulSoup
# import re


# def get_copywriter(tag):
#     whois = tag.find('div', clacc_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None

# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# # # row = soup.find("div", class_="name").text
# # # row = soup.find("div", class_='name')
# # # row = soup.find_all("div", {'class': 'name'})
# # # row = soup.find_all("div", class_="row")[1].find_all("div", class_='links')
# # # row = soup.find_all("div", {"data-set": "salary"})
# # # row = soup.find("div", text="Alena").parent
# # # row = soup.find("div", text="Alena").find_parent(class_="row")
# # # row = soup.find("div", id="whois3").find_previous_sibling()
# # # print(row)
# # copywriter = []
# # row = soup.find_all("div", class_="row")
# # for i in row:
# #     cw = get_copywriter(i)
# #     if cw:
# #         copywriter.append(cw)
# #
# # print(copywriter)
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)
import re
import csv

import requests
from bs4 import BeautifulSoup


# r = requests.get("https://ru.wordpress.org/")
# # print(r.headers['content-type'])
# # print(r.content)
# # r.encoding = 'utf-8'
# print(r.text)


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     # p1 = soup.find("header", id='masthead').find('p', class_='site-title').text
#     s = soup.find_all('section', class_='plugin-section')[1]
#     plugins = s.find_all('article')
#     for plugin in plugins:
#         name = plugin.find("h3").text  # заголовки плагинов
#         url = plugin.find('h3').find('a').get('href')  # доступ к ссылке
#         rating = plugin.find('span', class_='rating-count').find('a').text  # рейтинг пол
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()



# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['active'],
#                          data['cy']))
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     elements = soup.find_all('article', class_='plugin-card')
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             version = el.find('span', class_='tested-with').text
#             cy = refine_cy(version)
#         except ValueError:
#             cy = ''
#         print(cy)
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 5):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()




