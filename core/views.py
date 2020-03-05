from django.shortcuts import render,  get_object_or_404
from articles.models import Article, Element, Paragraph, MidiaVisual, YouTube
import json
from django.http import HttpResponse


    
def AllArticles_API (request):
    # Return all Aticles and your elements in Json format

    if request.method == 'GET':
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

#---------------------------------------------------------------------------------;
def Article_API (request, article_id):
    # Return a specifc Article in Json format
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_id)
        data = {}
        paragraphs = Paragraph.objects.all()
        midias = MidiaVisual.objects.all()
        youtubes = YouTube.objects.all()
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
        data_aticle = { 
                        'writer':article.writer_id.__str__(),
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

#---------------------------------------------------------------------------------;
def Article_API_Paragraph (request, article_id):
    # Return a specifc Article paragraphs in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_id)
        paragraphs = Paragraph.objects.all()
        data_paragraph = {}
        idx = 0
        for paragraph in paragraphs:
            if article.id == paragraph.article_id.id:
                data_paragraph[idx] = {
                                        'order':paragraph.order,
                                        'text':paragraph.text,
                                    }
                idx += 1

        dump = json.dumps(data_paragraph)
        return HttpResponse(dump, content_type='application/json')

#---------------------------------------------------------------------------------;
def Article_API_MidiaVisual (request, article_id):
    # Return a specifc Article midiavisual in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_id)
        midias = MidiaVisual.objects.all()
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

        dump = json.dumps(data_midia)
        return HttpResponse(dump, content_type='application/json')


#---------------------------------------------------------------------------------;
def Article_API_YouTube (request, article_id):
    # Return a specifc Article youtube in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_id)
        youtubes = YouTube.objects.all()
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
        
        dump = json.dumps(data_youtube)
        return HttpResponse(dump, content_type='application/json')