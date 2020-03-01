from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

#url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
html = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=날씨')
soup = bs(html.text, 'html.parser')
data1 = soup.find('div', {'class':'detail_box'})
#pprint(data1)
data2 = data1.findAll('dd')
pprint(data2)
data3 = data2[0].find('span')
print(data3.text)