import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.sogou.com/web?query=搞基建")
soup = BeautifulSoup(response.text, 'html.parser')
news_list = soup.find_all(name='div', class_='vrwrap')
print(news_list)