import datetime
from datetime import datetime
import time

import bs4
import requests
import logging

from articles.models import Article
from django.core.management import BaseCommand


class HabrParser:
    def __init__(self):
        self.session = requests.Session()

    @staticmethod
    def get_page(page: int = 1):
        """ Get html content from page """
        url = "https://habr.com/ru/top/page" + page.__str__() + "/"  # TODO Проверить на наличие страницы
        r = requests.get(url)
        return r.text

    @staticmethod
    def parse_links_heads(titles, links, text):
        """ fill in the lists of titles and links"""
        soup = bs4.BeautifulSoup(text, 'lxml')
        heads_links = soup.find_all('a', {'class': 'post__title_link'})
        for item in heads_links:
            titles.append(item.text)
            links.append(item['href'])
        return links, titles

    @staticmethod
    def parse_content(list_, contents_):  # TODO Удалить лишние символы
        """ fill in the list of contents with articles"""
        for url in list_:
            article = requests.get(url).text
            soup = bs4.BeautifulSoup(article, 'lxml')
            content_block = soup.find('div', {'class': 'post__text'})
            contents_.append(content_block.text[0:700])

    def parse_all(self):
        logging.info('Attempt date: ' + (datetime.now()).__str__() + '\n')
        start_time = time.time()
        self.get_data()
        logging.info('Time of working: ' + (time.time() - start_time).__str__())

    def get_pagination_limit(self, count_):
        """ Find the last page"""
        text = self.get_page(count_)
        soup = bs4.BeautifulSoup(text, 'lxml')
        page = soup.find('a', {'id': 'next_page'})
        if page is None:
            return False
        else:
            logging.info("Found page number: " + count_.__str__())
            return True

    def get_data(self):
        """ Get all data (headers, links, contents)"""
        logging.basicConfig(filename='myapp.log', level=logging.INFO)  # TODO Почиинить логирование
        count = 1
        title_storage, links_storage, articles_storage = [], [], []
        while True:
            title_temp, links_temp, contents_temp = [], [], []
            text = self.get_page(count)
            page_lim = self.get_pagination_limit(count)
            self.parse_links_heads(title_temp, links_temp, text)
            title_storage += title_temp
            links_storage += links_temp
            self.parse_content(links_temp, contents_temp)
            articles_storage += contents_temp
            if not page_lim:
                logging.info("page:" + count.__str__() + " successfully parsed")
                break
            logging.info("page:" + count.__str__() + " successfully parsed")
            count += 1

        for i in range(len(title_storage)):
            Article(
                title=title_storage[i],
                content=articles_storage[i],
                url=links_storage[i],
            ).save()


class Command(BaseCommand):
    help = 'Parse Habr'

    def handle(self, **args):
        test_parser = HabrParser()
        test_parser.parse_all()
