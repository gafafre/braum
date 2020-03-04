from django.shortcuts import render
from articles.models import Article, Element, Paragraph, MidiaVisual, YouTube
import json
from django.http import HttpResponse


    
def AllArticles (request):
    data = {}
    articles = Article.objects.all()
    paragraphs = Paragraph.objects.all()

    for article in articles:
        data_paragraph = {}
        cnt = 0
        for paragraph in paragraphs:
            if article.id == paragraph.article_id.id:
                data_paragraph[cnt] = {
                                        'order':paragraph.order,
                                        'text':paragraph.text,
                                      }
                cnt += 1

        data_aticle = { 'writer':article.writer_id.__str__(),
                        'title':article.title,
                        'subtitle':article.subtitle,
                        'publish_date':article.publish_date.__str__(),
                        'paragraphs':data_paragraph,
                        }
        data[article.id] = data_aticle
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


