from rest_framework.test import APITestCase
from django.test import TestCase
from .serializers import ArticleSerializer
from articles.models import Article


class ArticlesAPITest(APITestCase):
    def test_get(self):
        """Testing get request"""
        url = 'http://127.0.0.1:8000/articles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='test_title', content='test_content', url='test_url')

    def test_content_title(self):
        """Testing title content"""
        article = Article.objects.get(id=1)
        expected_article = f'{article.title}'
        self.assertEqual(article.title, expected_article)

    def test_body_content(self):
        """Testing body content"""
        article = Article.objects.get(id=1)
        expected_article = f'{article.content}'
        self.assertEqual(article.content, expected_article)

    def test_url_content(self):
        """Testing url content"""
        article = Article.objects.get(id=1)
        expected_article = f'{article.url}'
        self.assertEqual(article.url, expected_article)
