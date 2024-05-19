from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Project, Photo
from .forms import ProjectForm, PhotoForm, DateInput

def all_projects(request):
    """ Edit Project view """
    photos = Photo.objects.all()
    projects = Project.objects.all()
    template = 'projects/all_projects.html'
    context = {
        'projects': projects,
        'photos': photos,
    }

    return render(request, template, context)


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            # add success message
            return redirect(reverse('add_project'))
        #  add else + error msg
    else:
        form = ProjectForm()

    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_photo(request):
    
    projects = Project.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            # add success message
            return redirect(reverse('add_photo'))
        #  add else + error msg
    else:
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


def edit_project(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            # succes msg
            return redirect(reverse('all_projects'))
        # error msg
    form = ProjectForm(instance=project)
    # info msg?

    template = 'projects/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


def edit_photo(request, photo_id):

    projects = Project.objects.all()
    photo = get_object_or_404(Project, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            # succes msg
            return redirect(reverse('all_projects'))
        # error msg
    form = ProjectForm(instance=photo)
    # info msg?

    template = 'projects/edit_photo.html'
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template, context)