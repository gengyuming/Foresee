from bs4 import BeautifulSoup
from lxml import etree
import requests


url = 'https://www.lottery.gov.cn/kj/kjxq.html?319075'
response = requests.get(url)

# selector = etree.HTML(response.content)
#
# image_url = selector.xpath('/html/body/div/div[1]/div/article/div[2]/p/img')
# print(image_url.attrib['src'])

soup = BeautifulSoup(response.content, 'html.parser')
image = soup.find('img')

print(image)


