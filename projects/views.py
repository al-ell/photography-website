from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Photo
from .forms import ProjectForm, PhotoForm, DateInput

def all_projects(request):
    """ Wales Project view """
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, context, 'projects/all_projects.html')


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            # add success message
            
    else:
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
