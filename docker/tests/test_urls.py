from django.test import SimpleTestCase
from django.urls import reverse, resolve
from articles import views


class TestUrls(SimpleTestCase):

    print('\nTesting Docker Urls ...\n\n')

    def test_articles_url_is_resolved(self):
        url = reverse('articles')
        self.assertEquals(resolve(url).func, views.AllArticles_API)

    def test_specific_article_url_is_resolved(self):
        url = reverse('specific_article', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.Article_API)

    def test_article_paragraph_url_is_resolved(self):
        url = reverse('article_paragraph', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.Article_API_Paragraph)

    def test_article_midia_url_is_resolved(self):
        url = reverse('article_midia', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.Article_API_MidiaVisual)

    def test_article_yt_url_is_resolved(self):
        url = reverse('article_yt', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.Article_API_YouTube)
