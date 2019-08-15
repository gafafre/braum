# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader


def home(request):
    template = loader.get_template('./home.html')
    return HttpResponse(template.render())