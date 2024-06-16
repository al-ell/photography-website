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


# Only logged in superusers can access the views below
# Project and photo admin views
@login_required
def portfolio_admin(request):
    """ Project and photo management view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # display all project objects from the database
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # if form is valid, save
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which project to delete, send user to confirmation page to confirm action
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which photo to delete, send user to confirmation page to confirm action
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_admin')
        messages.success(request, f'Deleted {project.name} from Portfolio.')
    return render(request, 'projects/delete_project.html')


@login_required
def add_photo(request):
    """ Add photo view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))

    projects = Project.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # save the form
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # load specified photo form
    projects = Project.objects.all()
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            # check if valid, then save
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
    """ Delete photo confirmation view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which photo to delete, send user to confirmation page to confirm action
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        photo.delete()
        return redirect('portfolio_admin')
        messages.success(request, f'Deleted {photo.name}:{photo.friendly_name} from {photo.project}.')
    return render(request, 'projects/delete_photo.html')
