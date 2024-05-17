from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    """ Index view """
    
    return render(request, 'home/index.html')
