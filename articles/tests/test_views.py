from django.test import RequestFactory
from django.urls import reverse
from articles import views
from articles.models import Article
from writers.models import Writer
import pytest


@pytest.mark.django_db
class TestViews:
    writer = Writer.objects.get(pk=1)
    article_test = Article.objects.create(writer_id=writer, title='test', subtitle='test')

    def test_AllArticles_API_response(self):
        path = reverse('articles')
        request = RequestFactory().get(path)

        response = views.AllArticles_API(request)
        assert response.status_code == 200

    def test_Article_API_response(self):
        path = reverse('specific_article', kwargs={'article_slug': 'test'})
        request = RequestFactory().get(path)

        response = views.Article_API(request)
        assert response.status_code == 200

    def test_Article_API_Paragraph_response(self):
        path = reverse('article_paragraph', kwargs={'article_slug': 'test'})
        request = RequestFactory().get(path)

        response = views.Article_API_Paragraph(request)
        assert response.status_code == 200

    def test_Article_API_MidiaVisual_response(self):
        path = reverse('article_midia', kwargs={'article_slug': 'test'})
        request = RequestFactory().get(path)

        response = views.Article_API_MidiaVisual(request)
        assert response.status_code == 200

    def test_Article_API_YouTube_response(self):
        path = reverse('article_yt', kwargs={'article_slug': 'test'})
        request = RequestFactory().get(path)

        response = views.Article_API_YouTube(request)
        assert response.status_code == 200
