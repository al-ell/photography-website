from django.shortcuts import render
from .models import Project, Photo
from .forms import ProjectForm, PhotoForm

def all_projects(request):
    """ Wales Project view """
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, context, 'projects/all_projects.html')


def add_project(request):
    form = ProjectForm()
    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_photo(request):
    form = PhotoForm()
    template = 'projects/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def wales(request):
    """ Wales Project view """
    photos = Photo.objects.all()
    project = Project.objects.all()

    

    return render(request, 'projects/wales.html')


# def discovery(request):
#     """ Wales Project view """
    
#     return render(request, 'projects/discovery.html')
