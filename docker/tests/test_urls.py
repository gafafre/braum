from django.urrl import reverse, resolve
from articles.models import Article
from writers.models import Writer


class TestUrls:
    writer = Writer.objects.get(pk=1)
    article_test = Article.objects.create(writer_id=writer, title='test', subtitle='test')

    def test_articles_url(self):
        path = reverse('articles')
        assert resolve(path).view_name == 'articles'

    def test_specific_article_url(self):
        path = reverse('specific_article', kwargs={'article_slug': 'test'})
        assert resolve(path).view_name == 'specific_article'

    def test_article_paragraph_url(self):
        path = reverse('article_paragraph', kwargs={'article_slug': 'test'})
        assert resolve(path).view_name == 'article_paragraph'

    def test_article_midia_url(self):
        path = reverse('article_midia', kwargs={'article_slug': 'test'})
        assert resolve(path).view_name == 'article_midia'

    def test_article_yt_url(self):
        path = reverse('article_yt', kwargs={'article_slug': 'test'})
        assert resolve(path).view_name == 'article_yt'
