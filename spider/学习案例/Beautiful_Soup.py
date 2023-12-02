from bs4 import BeautifulSoup

with open("./test.html") as fp:
    html_doc = fp.read()

soup = BeautifulSoup(html_doc, 'html.parser')

div_node = soup.find("div", id='content')

# links = soup.find_all('a')
links = div_node.find_all('a')

for link in links:
    print(link.name, link['href'], link.get_text())