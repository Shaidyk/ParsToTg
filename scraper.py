import json
import requests

from bs4 import BeautifulSoup

from config import login_data, user_agent


class ParserTesmania:  # noqa
    login_link = 'https://www.tesmanian.com/account'
    link = 'https://www.tesmanian.com/'
    headers = {
        'user_agent': user_agent
    }
    spacex_dict = {}
    tesla_dict = {}

    def __init__(self):
        self.session = requests.Session()
        self.login()
        self.div_id_spacex = 'shopify-section-1581705557561'
        self.div_id_tesla = 'shopify-section-1581706887820'
        self.response = self.get_response()
        self.soup = self.get_soup()

    def login(self):
        self.session.post(self.login_link, data=login_data, headers=self.headers)

    def get_response(self):
        self.response = self.session.get(self.link, headers=self.headers).text
        return self.response

    def get_soup(self):
        self.soup = BeautifulSoup(self.response, 'lxml')
        return self.soup

    def get_spacex_all(self):
        block = self.soup.find('div', id=self.div_id_spacex)
        articles = block.find_all('h3', class_='sub_title')

        for article in articles:
            article_title = article.find('a').text
            article_url = 'https://www.tesmanian.com/' + article.find('a').get('href')
            article_id = article_url.split('/')[-1]
            self.spacex_dict[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }

        with open('spacex_article.json', 'w') as file:
            json.dump(self.spacex_dict, file, indent=4, ensure_ascii=False)

    def get_tesla_all(self):
        block = self.soup.find('div', id=self.div_id_tesla)
        articles = block.find_all('h3', class_='sub_title')

        for article in articles:
            article_title = article.find('a').text
            article_url = 'https://www.tesmanian.com/' + article.find('a').get('href')
            article_id = article_url.split('/')[-1]
            self.tesla_dict[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }

        with open('tesla_article.json', 'w') as file:
            json.dump(self.tesla_dict, file, indent=4, ensure_ascii=False)

    def get_spacex(self):
        try:
            with open('spacex_article.json') as file:
                self.spacex_dict = json.load(file)
        except FileNotFoundError:
            with open('spacex_article.json', 'w') as file:
                json.dump(self.spacex_dict, file, indent=4, ensure_ascii=False)

        block = self.soup.find('div', id=self.div_id_spacex)
        articles = block.find_all('h3', class_='sub_title')

        new_articles = {}
        for article in articles:
            article_title = article.find('a').text
            article_url = 'https://www.tesmanian.com/' + article.find('a').get('href')
            article_id = article_url.split('/')[-1]

            if article_id in self.spacex_dict:
                continue
            else:
                self.spacex_dict[article_id] = {
                    'article_title': article_title,
                    'article_url': article_url
                }

                new_articles[article_id] = {
                    'article_title': article_title,
                    'article_url': article_url
                }

        with open('spacex_article.json', 'w') as file:
            json.dump(self.spacex_dict, file, indent=4, ensure_ascii=False)

        return new_articles

    def get_tesla(self):
        try:
            with open('tesla_article.json') as file:
                self.tesla_dict = json.load(file)
        except FileNotFoundError:
            with open('tesla_article.json', 'w') as file:
                json.dump(self.tesla_dict, file, indent=4, ensure_ascii=False)

        block = self.soup.find('div', id=self.div_id_tesla)
        articles = block.find_all('h3', class_='sub_title')

        new_articles = {}
        for article in articles:
            article_title = article.find('a').text
            article_url = 'https://www.tesmanian.com/' + article.find('a').get('href')
            article_id = article_url.split('/')[-1]

            if article_id in self.tesla_dict:
                continue
            else:
                self.tesla_dict[article_id] = {
                    'article_title': article_title,
                    'article_url': article_url
                }

                new_articles[article_id] = {
                    'article_title': article_title,
                    'article_url': article_url
                }

        with open('tesla_article.json', 'w') as file:
            json.dump(self.tesla_dict, file, indent=4, ensure_ascii=False)

        return new_articles


t = ParserTesmania()
t.get_tesla()