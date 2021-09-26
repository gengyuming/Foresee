from bs4 import BeautifulSoup
from lxml import etree
import requests


url = 'https://www.sporttery.cn/kj/lskj/319075.html'
response = requests.get(url)



soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
img_tag = soup.find('img')
img_src = img_tag.attrs['src']
img_resp = requests.get('http:' + img_src)
print(img_tag)
print(img_src)


print(img_resp.content)


