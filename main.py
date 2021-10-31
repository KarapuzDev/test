import bs4
import requests
from bs4 import BeautifulSoup
import csv

from requests.exceptions import Timeout
from requests.sessions import session

lisst_quotes = []
lisst_quotes1 = []
lisst_quotes2 = []

result_list = []
proxi_list = []


url_proxi = "https://www.livelib.ru/reviews/experts/"

# proxiesDict = {

# print(proxiesDict.items())
list_proxy = ["178.219.183.32"]
for k in list_proxy:
    proxiesDict = {"http": '204.13.164.179', "https": k}
    r = requests.get("https://www.livelib.ru/reviews/experts/", proxies=proxiesDict)

# for k in proxiesDict:
#     print(k)


# r = requests.get("https://hidemy.name/ru/", proxies=proxiesDict)

# g = 1

# while g <= 800:
#     # url = 'https://www.livelib.ru/reviews/experts/~'+str(g)+'#reviews'
#     url = 'https://www.livelib.ru/reviews/~'+str(g)+'#reviews'
#     response = requests.get(url)
#     response.encoding = 'utf8'
#     soup = BeautifulSoup(response.text, 'lxml')

#     quotes = soup.find_all('span', class_='lenta-card__mymark')

#     quotes1 = soup.find_all('a', class_='lenta-card__book-title')
#     quotes2 = soup.find_all('div', id='lenta-card__text-review-escaped')
#     print('страница ',g,' длина ',len(quotes1))
#     print(soup)

#     for mex in quotes1:
#         lisst_quotes.append(mex.get_text())

#     for mex in quotes2:
#         lisst_quotes1.append(mex.get_text())

#     for mex in quotes:
#         # print(mex.get_text().strip())
#         lisst_quotes2.append(mex.get_text().strip())
#         g += 1

# i = 0
# while i < len(lisst_quotes):
#     result_list.append([lisst_quotes[i], lisst_quotes1[i], lisst_quotes2[i], ])
#     i += 1



# # print(len(lisst_quotes))
# # print(len(lisst_quotes1))
# # print(len(lisst_quotes2))

# # print(result_list)


# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
#     file_writer = csv.writer(w_file, delimiter = "@")#, lineterminator="\r")
#     for row in result_list:
#         file_writer.writerow(row)

# print(len(lisst_quotes2))