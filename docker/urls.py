from django.conf.urls.static import static
from home.views import home
from django.contrib import admin
from django.urls import path
from django.conf import settings
from articles import views

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('articles/', views.AllArticles_API, name='articles'),
    path('articles/<str:article_slug>/', views.Article_API, name='specific_article'),
    path('articles/<str:article_slug>/paragraph/', views.Article_API_Paragraph, name='article_paragraph'),
    path('articles/<str:article_slug>/midiavisual/', views.Article_API_MidiaVisual, name='article_midia'),
    path('articles/<str:article_slug>/youtube/', views.Article_API_YouTube, name='article_yt'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
