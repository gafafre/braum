from django.contrib import admin
from .models import Article, Element, MidiaVisual, Paragraph, YouTube

admin.site.register(Article)
admin.site.register(MidiaVisual)
admin.site.register(Paragraph)
admin.site.register(YouTube)