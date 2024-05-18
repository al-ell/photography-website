from django.shortcuts import render
from .models import Project, Photo

def all_projects(request):
    """ Wales Project view """
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, context, 'projects/all_projects.html')


def wales(request):
    """ Wales Project view """
    photos = Photo.objects.all()
    project = Project.objects.all()

    

    return render(request, 'projects/wales.html')


# def discovery(request):
#     """ Wales Project view """
    
#     return render(request, 'projects/discovery.html')
