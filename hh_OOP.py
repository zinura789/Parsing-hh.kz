import requests
from bs4 import BeautifulSoup
import csv
import os
HEADERS = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
PARAMS = {'area': '40', 'clusters': 'true', 'currency_code': 'KZT', 'exp_period': 'all_time', 'logic': 'normal', 'no_magic': 'False',
              'order_by': 'relevance', 'pos': 'position', 'ored_clusters': 'True', 'st': 'resumeSearch','from': 'suggest_post'}
class Html:
    def __init__(self,keyword, url = 'https://hh.kz/search/resume', headers=HEADERS, params=PARAMS):
        self.keyword = keyword
        self.url = url
        self.headers = headers
        self.params = params
    def get_html(self, ):
        self.params.update({'text' : self.keyword})
        response = requests.get(self.url, headers=self.headers, params=self.params).text
        html = BeautifulSoup(response, 'html.parser')
        return html

class Content:
    def get_content(self, html):
        self.html = Html(Parser.keyword).get_html()
        items = self.html.find_all('div', class_='resume-search-item')
        content = []
        for item in items:
            content.append({
                'title': item.find('a', class_='resume-search-item__name').get_text(strip=True),
                'link': 'https://hh.kz' + item.find('a', class_='resume-search-item__name').get('href'),
                'experience': item.find('div', class_='resume-search-item__description-content').get_text(strip=True)
            })
        return content
class Save:
    def save_file(self,items, path):
        self.items = items
        self.path = path
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Должность', 'Ссылка на резюме','Опыт работы'])
            for item in self.items:
                writer.writerow([item['title'], item['link'], item['experience']])

class Parser:
    keyword = 'Директор по маркетингу'

    def get_pages_count(self):
        html = Html(Parser.keyword).get_html()
        pagination = html.find_all('span', class_='pager-item-not-in-short-range')
        if pagination:
            return int(pagination[-1].get_text())
        else:
            return None

    def parse(self):
        last_page = self.get_pages_count()
        resumes = []
        for page in range(last_page):
            print(f'Парсинг страницы {page} из {last_page}...')
            params_with_page_number = PARAMS.update({'page' : page})
            html = Html(Parser.keyword, params = params_with_page_number)
            resumes.extend(Content().get_content(html))
        print(f'Получено {len(resumes)} резюме')

        Save().save_file(resumes, 'resumes.csv')
        os.startfile('resumes.csv')
a = Parser()
a.parse()



