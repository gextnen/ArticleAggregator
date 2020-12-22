import datetime
from datetime import datetime
import time
from rest_framework import status
import bs4
import requests
import logging

from articles.models import Article
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class HabrParser:
    def __init__(self):
        self.session = requests.Session()

    def get_page(self, page: int = 1):
        """ Get html content from page """
        url = "https://habr.com/ru/top/page" + page.__str__() + "/"
        response = requests.get(url).status_code
        if response == status.HTTP_200_OK:
            r = requests.get(url)
            logging.debug('200 OK')
            return r.text
        elif response >= 500:
            logging.error('Error: ', response.__str__())
            raise TypeError(response)
        elif response >= 400:
            logging.warning('Error: ' + response.__str__())
            raise TypeError(response)

    @staticmethod
    def parse_links_heads(titles, links, text):
        """ fill in the lists of titles and links"""
        logging.debug('start function: parse_links_heads')
        soup = bs4.BeautifulSoup(text, 'lxml')
        heads_links = soup.find_all('a', {'class': 'post__title_link'})
        for item in heads_links:
            titles.append(item.text)
            links.append(item['href'])
        logging.debug('end function: parse_links_heads')
        return links, titles

    @staticmethod
    def parse_content(list_, contents_):
        """ fill in the list of contents with articles"""
        logging.debug('start function: parse_content')
        for url in list_:
            article = requests.get(url).text
            soup = bs4.BeautifulSoup(article, 'lxml')
            content_block = soup.find('div', {'class': 'post__text'})
            contents_.append(content_block.text)
        logging.debug('end function: parse_content')

    def parse_all(self):
        logging.info('Attempt date: ' + (datetime.now()).__str__() + '\n')
        start_time = time.time()
        self.get_data()
        logging.info('Time of working: ' + (time.time() - start_time).__str__())

    def get_pagination_limit(self, count_):
        """ Find the last page"""
        logging.debug('start function: get_pagination_limit')

        text = self.get_page(count_)
        soup = bs4.BeautifulSoup(text, 'lxml')
        page = soup.find('a', {'id': 'next_page'})
        if page is None:
            return False
        else:
            logging.debug("Found page number: " + count_.__str__())
            return True

    def get_data(self):
        """ Get all data (headers, links, contents)"""
        logging.debug('start function: get_pagination_limit')
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
                logging.debug("page:" + count.__str__() + " successfully parsed")
                break
            logging.debug("page:" + count.__str__() + " successfully parsed")
            count += 1
        logging.debug('end function: get_pagination_limit')

        logging.debug('Start writing data to the model Article')
        for i in range(len(title_storage)):
            Article(
                title=title_storage[i],
                content=articles_storage[i],
                url=links_storage[i],
            ).save()
        logging.debug('End writing data to the model Article')


class Command(BaseCommand):
    help = 'Parse Habr'

    def handle(self, **args):
        test_parser = HabrParser()
        test_parser.parse_all()
