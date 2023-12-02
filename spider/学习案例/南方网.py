import requests
from bs4 import BeautifulSoup

url = 'https://news.southcn.com/node_179d29f1ce?cms_node_post_list_page='

r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'html.parser')
div_node = soup.find('div', class_='m-lists')
print(div_node)
links = div_node.find_all('a')
for item in links:
    print(item.name,  item['href'], item.get_text())