import requests

coin_list = []

# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text.split("<span>")
# for elem in response_text:
#     if elem.startswith('$'):
#         for elem2 in elem.split("</span>"):
#             if elem2.startswith("$"):
#                 coin_list.append(elem2)
#
# btc = float(coin_list[8].replace('$', '').replace(',', ''))
# print(btc)


response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, features='html.parser')
btc = soup.find("span", {"class", "sc-c1554bc0-0 RbQXx base-text"}).text.replace('$', '').replace(',', '')
print(btc)


# https://bank.gov.ua/ua/markets/exchangerates