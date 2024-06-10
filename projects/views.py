from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Photo
from .forms import ProjectForm, PhotoForm

from shop.models import Prints

def wales(request):
    """ Wales Project view """
    photos = Photo.objects.all()
    projects = Project.objects.all()

    template = 'projects/wales.html'
    context = {
        'photos': photos,
        'projects': projects,

    }

    return render(request, template, context)


def discovery(request):
    """ Discovery Project view """
    photos = Photo.objects.all()
    projects = Project.objects.all()

    template = 'projects/discovery.html'
    context = {
        'photos': photos,
        'projects': projects,

    }

    return render(request, template, context)


# Project and photo admin views
@login_required
def portfolio_admin(request):
    """ Project and photo management view """
    photos = Photo.objects.all()
    projects = Project.objects.all()
    template = 'projects/portfolio_admin.html'
    context = {
        'projects': projects,
        'photos': photos,
    }

    return render(request, template, context)


@login_required
def add_project(request):
    """ Add project view """

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, f'Added {project.name} to Portfolio.')
            return redirect(reverse('portfolio_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = ProjectForm()

    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, project_id):
    """ Edit project view """
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated {project.name} to Portfolio.')
            return redirect('portfolio_admin')
        else:
            messages.error(request, f'Please make sure form is valid.')
    form = ProjectForm(instance=project)
    messages.info(request, f'Updating {project.name} in Portfolio.')

    template = 'projects/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


@login_required
def delete_project(request, project_id):
    """ Delete project view """
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, f'Deleted {project.name} from Portfolio.')
    return redirect(reverse('portfolio_admin'))


@login_required
def add_photo(request):
    """ Add photo view """
    projects = Project.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            messages.success(request, f'Added {photo.name} to {photo.project}.')
            return redirect(reverse('portfoio_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = PhotoForm()

    template = 'projects/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_photo(request, photo_id):
    """ Edit photo view """
    projects = Project.objects.all()
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, f'Edited {photo.name} in {photo.project}.')
            return redirect(reverse('portfolio_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    form = ProjectForm(instance=photo)
    messages.success(request, f'Updating {photo.name} in {photo.project}.')

    template = 'projects/edit_photo.html'
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template, context)


@login_required
def delete_photo(request, photo_id):
    """ Delete photo view """
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()
    messages.success(request, f'Deleted {photo.name} from {photo.project}.')
    return redirect(reverse('portfolio_admin'))
