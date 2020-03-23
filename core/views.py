from django.shortcuts import get_object_or_404
from articles.models import Article, Paragraph, MidiaVisual, YouTube
import json
from django.http import HttpResponse


def AllArticles_API(request):
    # Return all Aticles and your elements in Json format

    if request.method == 'GET':
        data = []
        articles = Article.objects.all()
        paragraphs = Paragraph.objects.all()
        midias = MidiaVisual.objects.all()
        youtubes = YouTube.objects.all()

        for article in articles:
            # Get All article paragraphs
            data_paragraph = []
            for paragraph in paragraphs:
                if article.id == paragraph.article_id.id:
                    data_paragraph.append({
                                            'order':paragraph.order,
                                            'text':paragraph.text,
                                        })

            #Get All article MidiaVisuals
            data_midia = []
            for midia in midias:
                if article.id == midia.article_id.id:
                    data_midia.append({ 
                                        'order':midia.order,
                                        'src':midia.src,
                                        'alt':midia.alt,
                                        'width':midia.width,
                                        'height':midia.height,
                                        'src_link':midia.src_link,
                                        })

            #Get All article YouTube
            data_youtube = []
            for youtube in youtubes:
                if article.id == youtube.article_id.id:
                    data_youtube.append({
                                            'order':youtube.order,
                                            'src':youtube.src,
                                            'autoplay':youtube.autoplay,
                                            'loop':youtube.loop,
                                            'start':youtube.start,
                                        })

            #Create Article Data with all models
            data_aticle = { 'id':article.id,
                            'slug':article.slug,
                            'writer':article.writer_id.__str__(),
                            'title':article.title,
                            'subtitle':article.subtitle,
                            'publish_date':article.publish_date.__str__(),
                            'Paragraph':data_paragraph,
                            'MediaVisual':data_midia,
                            'YouTube':data_youtube,
                            }
            data.append(data_aticle)


        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

#---------------------------------------------------------------------------------;
def Article_API (request, article_slug):
    # Return a specifc Article in Json format
    if request.method == 'GET':
        article = get_object_or_404(Article, slug=article_slug)
        data = []
        paragraphs = Paragraph.objects.all()
        midias = MidiaVisual.objects.all()
        youtubes = YouTube.objects.all()
        # Get All article paragraphs
        data_paragraph = []
        for paragraph in paragraphs:
            if article.id == paragraph.article_id.id:
                data_paragraph.append({
                                        'order':paragraph.order,
                                        'text':paragraph.text,
                                    })

        #Get All article MidiaVisuals
        data_midia = []
        for midia in midias:
            if article.id == midia.article_id.id:
                data_midia.append({ 
                                    'order':midia.order,
                                    'src':midia.src,
                                    'alt':midia.alt,
                                    'width':midia.width,
                                    'height':midia.height,
                                    'src_link':midia.src_link,
                                    })

        #Get All article YouTube
        data_youtube = []
        for youtube in youtubes:
            if article.id == youtube.article_id.id:
                data_youtube.append({
                                        'order':youtube.order,
                                        'src':youtube.src,
                                        'autoplay':youtube.autoplay,
                                        'loop':youtube.loop,
                                        'start':youtube.start,
                                    })

        #Create Article Data with all models
        data_aticle = { 
                        'id':article.id,
                        'writer':article.writer_id.__str__(),
                        'title':article.title,
                        'subtitle':article.subtitle,
                        'publish_date':article.publish_date.__str__(),
                        'Paragraph':data_paragraph,
                        'MediaVisual':data_midia,
                        'YouTube':data_youtube,
                        }
        data.append(data_aticle)


        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

#---------------------------------------------------------------------------------;
def Article_API_Paragraph (request, article_slug):
    # Return a specifc Article paragraphs in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, slug=article_slug)
        paragraphs = Paragraph.objects.all()
        data_paragraph = []
        for paragraph in paragraphs:
            if article.id == paragraph.article_id.id:
                data_paragraph.append({
                                        'order':paragraph.order,
                                        'text':paragraph.text,
                                    })

        dump = json.dumps(data_paragraph)
        return HttpResponse(dump, content_type='application/json')

#---------------------------------------------------------------------------------;
def Article_API_MidiaVisual (request, article_slug):
    # Return a specifc Article midiavisual in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, slug=article_slug)
        midias = MidiaVisual.objects.all()
        data_midia = []
        for midia in midias:
            if article.id == midia.article_id.id:
                data_midia.append({ 
                                    'order':midia.order,
                                    'src':midia.src,
                                    'alt':midia.alt,
                                    'width':midia.width,
                                    'height':midia.height,
                                    'src_link':midia.src_link,
                                    })

        dump = json.dumps(data_midia)
        return HttpResponse(dump, content_type='application/json')


#---------------------------------------------------------------------------------;
def Article_API_YouTube (request, article_slug):
    # Return a specifc Article youtube in Json format

    if request.method == 'GET':
        article = get_object_or_404(Article, slug=article_slug)
        youtubes = YouTube.objects.all()
        data_youtube = []
        for youtube in youtubes:
            if article.id == youtube.article_id.id:
                data_youtube.append({
                                        'order':youtube.order,
                                        'src':youtube.src,
                                        'autoplay':youtube.autoplay,
                                        'loop':youtube.loop,
                                        'start':youtube.start,
                                    })
        
        dump = json.dumps(data_youtube)
        return HttpResponse(dump, content_type='application/json')