from django.shortcuts import render
from projects.models import Photo


def index(request):
    """ Index view """
    photo_ids = [47, 8, 70, 31, 1, 31]
    photos = Photo.objects.filter(id__in=photo_ids)


    template = 'home/index.html'
    context = {
        'photos': photos,
    }
    
    return render(request, template, context)
