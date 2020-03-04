from django.shortcuts import render
from articles.models import Article, Element, Paragraph, MidiaVisual, YouTube
import json
from django.http import HttpResponse


    
def AllArticles (request):
    data = {}
    articles = Article.objects.all()
    paragraphs = Paragraph.objects.all()
    midias = MidiaVisual.objects.all()
    youtubes = YouTube.objects.all()

    for article in articles:
        # Get All article paragraphs
        data_paragraph = {}
        idx = 0
        for paragraph in paragraphs:
            if article.id == paragraph.article_id.id:
                data_paragraph[idx] = {
                                        'order':paragraph.order,
                                        'text':paragraph.text,
                                      }
                idx += 1

        #Get All article MidiaVisuals
        data_midia = {}
        idx = 0
        for midia in midias:
            if article.id == midia.article_id.id:
                data_midia[idx] = { 
                                    'order':midia.order,
                                    'src':midia.src,
                                    'alt':midia.alt,
                                    'width':midia.width,
                                    'height':midia.height,
                                    'src_link':midia.src_link,
                                    }
                idx += 1

        #Get All article YouTube
        data_youtube = {}
        idx = 0
        for youtube in youtubes:
            if article.id == youtube.article_id.id:
                data_youtube[idx] = {
                                        'order':youtube.order,
                                        'src':youtube.src,
                                        'autoplay':youtube.autoplay,
                                        'loop':youtube.loop,
                                        'start':youtube.start,
                                      }
                idx += 1

        #Create Article Data with all models
        data_aticle = { 'writer':article.writer_id.__str__(),
                        'title':article.title,
                        'subtitle':article.subtitle,
                        'publish_date':article.publish_date.__str__(),
                        'Paragraph':data_paragraph,
                        'MediaVisual':data_midia,
                        'YouTube':data_youtube,
                        }
        data[article.id] = data_aticle


    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


