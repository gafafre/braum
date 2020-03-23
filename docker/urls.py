from django.conf.urls.static import static
from home.views import home
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.conf import settings
from core import views



urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('articles/', views.AllArticles_API),
    path('articles/<str:article_slug>/', views.Article_API),
    path('articles/<str:article_slug>/paragraph/', views.Article_API_Paragraph),
    path('articles/<str:article_slug>/midiavisual/', views.Article_API_MidiaVisual),
    path('articles/<str:article_slug>/youtube/', views.Article_API_YouTube),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
