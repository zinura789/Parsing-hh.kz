import requests
from bs4 import BeautifulSoup

class GetHtml:
    HEADERS = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    PARAMS = {
        'area': '40',
        'clusters': 'true',
        'currency_code': 'KZT',
        'exp_period': 'all_time',
        'logic': 'normal',
        'no_magic': 'false',
        'order_by': 'relevance',
        'pos': 'position'
    }

    def html(self, url, keyword):
        self.url = url
        self.keyword = keyword
        response = requests.get(self.url, headers=GetHtml.HEADERS, params=GetHtml.PARAMS.update({'text' : self.keyword})).text
        html = BeautifulSoup(response, 'html.parser')
        return html

a = GetHtml()
html = a.html('https://hh.kz/search/resume', 'директор по маркетингу')

#код ниже для проверки корректности html 
items = html.find_all('div', class_='resume-search-item')
content = []
for item in items:
    HOST = 'https://hh.kz'
    content.append({
        'title': item.find('a', class_='resume-search-item__name').get_text(strip=True),
        'link': HOST + item.find('a', class_='resume-search-item__name').get('href'),
        'experience': item.find('div', class_='resume-search-item__description-content').get_text(strip=True)
    })
print(content)
