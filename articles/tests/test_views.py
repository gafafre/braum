from django.test import TestCase, Client
from django.urls import reverse
from articles.models import Article, MidiaVisual, YouTube, Paragraph
from writers.models import Writer
from django.contrib.auth.models import User


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
        self.test_user = User.objects.create_user('tester', 'tester@test.com', 'testerpassword')
        self.test_writer = Writer.objects.create(user=self.test_user)
        self.article1 = Article.objects.create(
            writer_id=self.test_writer,
            title='test title',
            subtitle='test subtitle',
        )
        self.midia1 = MidiaVisual.objects.create(
            article_id=self.article1,
            order=1.0,
            src='src',
            alt='alt',
            width=100,
            height=100,
            src_link='link'
        )
        self.paragraph1 = Paragraph.objects.create(
            article_id=self.article1,
            order=1.0,
            text='text'
        )
        self.youtube1 = YouTube.objects.create(
            article_id=self.article1,
            order=1.0,
            src='src',
            autoplay=True,
            loop=True
        )

    def test_AllArticles_API_GET(self):
        response = self.client.get(self.articles_url)
        result = (b'"slug": "test-title", "writer": "tester",'
                  b' "title": "test title", "subtitle": "test subtitle",'
                  b' "publish_date": "None", "Paragraph": [{"order": 1.0, "text": "text"}],'
                  b' "MediaVisual": [{"order": 1.0, "src": "src", "alt": "alt", "width": 100,'
                  b' "height": 100, "src_link": "link"}], "YouTube": [{"order": 1.0,'
                  b' "src": "src", "autoplay": true, "loop": true, "start": null}]')
        self.assertEquals(response.status_code, 200)
        self.assertIn(result, response.content)

    def test_Article_API_GET(self):
        response = self.client.get(self.specific_article_url)
        result = (b'"writer": "tester", "title": "test title",'
                  b' "subtitle": "test subtitle", "publish_date": "None",'
                  b' "Paragraph": [{"order": 1.0, "text": "text"}],'
                  b' "MediaVisual": [{"order": 1.0, "src": "src", "alt": "alt",'
                  b' "width": 100, "height": 100, "src_link": "link"}],'
                  b' "YouTube": [{"order": 1.0, "src": "src", "autoplay": true,'
                  b' "loop": true, "start": null}]')
        self.assertEquals(response.status_code, 200)
        self.assertIn(result, response.content)

    def test_Article_API_Paragraph_GET(self):
        response = self.client.get(self.article_paragraph_url)
        result = b'[{"order": 1.0, "text": "text"}]'
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, result)

    def test_Article_API_MidiaVisual_GET(self):
        response = self.client.get(self.article_midia_url)
        result = (b'[{"order": 1.0, "src": "src", "alt": "alt", "width": 100,'
                  b' "height": 100, "src_link": "link"}]')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, result)

    def test_Article_API_YouTube_GET(self):
        response = self.client.get(self.article_yt_url)
        result = b'[{"order": 1.0, "src": "src", "autoplay": true, "loop": true, "start": null}]'
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, result)
