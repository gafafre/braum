from articles.models import Article
from writers.models import Writer
import pytest


@pytest.mark.django_db
class TestModels:

    def setUp(self):
        self.writer = Writer.objects.get(pk=1)
        self.article_test = Article.objects.create(writer_id=self.writer, title='test', subtitle='test')

    def test_create_article(self):
        assert self.article_test.__str__ == 'test'
