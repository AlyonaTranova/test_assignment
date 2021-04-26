import urllib.parse
from bs4 import BeautifulSoup
import requests
from transliterate import translit
import json


class ParsingApp:

    def __init__(self):

        self.app_url = []
        self.test = {}

    def parsing(self, search_app):
        word_request = urllib.parse.quote(search_app)
        response = requests.get('https://play.google.com/store/search?q=' + word_request + '&c=apps')
        eng_word_request = translit(search_app, 'ru', reversed=True)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_applications = html_doc.find_all('div', {'class': 'b8cIId ReQCgd Q9MA7b'})
            for app in list_of_applications:
                if word_request or eng_word_request in app.a.text.lower():
                    url_app = app.a['href']
                    self.app_url.append(url_app)
        return self.app_url

    def info_parsing(self, web_list):
        for website in web_list:
            response_1 = requests.get('https://play.google.com' + website)
            if response_1.status_code == 200:
                try:
                    html_doc = BeautifulSoup(response_1.text, features='html.parser')
                    url_of_app = response_1.url
                    name = html_doc.find('h1', {'class': 'AHFaub'})
                    author = html_doc.find('a', {'class', "hrTbp R8zArc"})
                    last_upgrade = html_doc.find('span', {'class': 'htlgb'})
                    category = html_doc.find('a', {'itemprop': 'genre'})
                    average_grade = html_doc.find('div', {'class': 'BHMmbe'})
                    views = html_doc.find('span', {'class': 'EymY4b'})
                    description = html_doc.find('div', {'jsname': 'sngebd'})

                    name_json = name.text
                    last_upgrade_json = last_upgrade.text
                    author_json = author.text
                    category_json = category.text
                    av_grade_json = average_grade.text
                    views_json = views.text
                    description_json = description.text

                    data = {
                        'Title': name_json,
                        'URL': url_of_app,
                        'Author': author_json,
                        'Category': category_json,
                        'Description': description_json,
                        'Average_grade': av_grade_json,
                        'Views': views_json,
                        'Last_update': last_upgrade_json
                    }

                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        print(data)
                except:
                    pass


if __name__ == '__main__':
    name_of_app = input((str('Введите название приложения: ')))
    parsing = ParsingApp()
    website_list = parsing.parsing(name_of_app)
    parsing.info_parsing(website_list)
