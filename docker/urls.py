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
    path('articles/<int:article_id>/', views.Article_API),
    path('articles/<int:article_id>/paragraph/', views.Article_API_Paragraph),
    path('articles/<int:article_id>/midiavisual/', views.Article_API_MidiaVisual),
    path('articles/<int:article_id>/youtube/', views.Article_API_YouTube),
    # path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
