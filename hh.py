import requests
from bs4 import BeautifulSoup
import csv
import os
HOST = 'https://hh.kz'
FILE = 'resumes.csv'
URL = 'https://hh.kz/search/resume'
HEADERS = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
PARAMS = {
    'area': '40',
    'clusters': 'true',
    'currency_code': 'KZT',
    'exp_period': 'all_time',
    'logic': 'normal',
    'no_magic': 'false',
    'order_by': 'relevance',
    'pos': 'position',
    'text': 'директор по маркетингу'
}

#experience = ['between1And3', 'between3And6', 'moreThan6']

def get_html(url, params=None):
    response = requests.get(URL, headers=HEADERS, params=PARAMS).text
    html = BeautifulSoup(response, 'html.parser')
    return html

def get_pages_count(html):
    pagination = html.find_all('span', class_='pager-item-not-in-short-range')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return None
def get_content(html):
    items = html.find_all('div', class_='resume-search-item')
    content = []
    for item in items:
        content.append({
            'title': item.find('a', class_='resume-search-item__name').get_text(strip=True),
            'link': HOST + item.find('a', class_='resume-search-item__name').get('href'),
            'experience': item.find('div', class_='resume-search-item__description-content').get_text(strip=True)
        })
    return content

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Должность', 'Ссылка на резюме','Опыт работы'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['experience']])

def parse():
    html = get_html(URL)
    last_page = get_pages_count(html)
    resumes = []
    for page in range(last_page):
        print(f'Парсинг страницы {page} из {last_page}...')
        html = get_html(URL, params=PARAMS.update({'page' : page}))
        resumes.extend(get_content(html))
    save_file(resumes, FILE)
    print(f'Получено {len(resumes)} резюме')
    os.startfile(FILE)

parse()
