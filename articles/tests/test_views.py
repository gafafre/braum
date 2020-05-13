from django.test import TestCase, Client
from django.urls import reverse
from articles.models import Article, Element, MidiaVisual, YouTube, Paragraph
from writers.models import Writer
from django.contrib.auth.models import User
import json
import datetime


class TestViews(TestCase):

    print('\nTesting Articles Views ...\n')

    def setUp(self):
        self.client = Client()
        self.articles_url = reverse('articles')
        self.specific_article_url = reverse('specific_article', args=['test-title'])
        self.article_paragraph_url = reverse('article_paragraph', args=['test-title'])
        self.article_midia_url = reverse('article_midia', args=['test-title'])
        self.article_yt_url = reverse('article_yt', args=['test-title'])

        # Creating a temporary Article for tests
        test_user = User.objects.create_user('tester', 'tester@test.com', 'testerpassword')
        test_writer = Writer.objects.create(user=test_user)
        self.article1 = Article.objects.create(
            writer_id=test_writer,
            title='test title',
            subtitle='test subtitle',
            # publish_date=datetime.datetime(2020, 5, 12, 23, 40, 51), # not necessary
            # slug='test-title' # not necessary
        )

    def test_AllArticles_API_GET(self):
        response = self.client.get(self.articles_url)
        self.assertEquals(response.status_code, 200)

    def test_Article_API_GET(self):
        response = self.client.get(self.specific_article_url)
        self.assertEquals(response.status_code, 200)

    def test_Article_API_Paragraph_GET(self):
        response = self.client.get(self.article_paragraph_url)
        self.assertEquals(response.status_code, 200)

    def test_Article_API_MidiaVisual_GET(self):
        response = self.client.get(self.article_midia_url)
        self.assertEquals(response.status_code, 200)

    def test_Article_API_YouTube_GET(self):
        response = self.client.get(self.article_yt_url)
        self.assertEquals(response.status_code, 200)
