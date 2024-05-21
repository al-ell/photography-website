from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Prints
from .forms import PrintsForm


def all_prints(request):
    """ Shop view """
    prints = Prints.objects.all()
    category = Category.objects.all()

    template = 'shop/prints.html'
    context = {
        'prints': prints,
        'category': category,
    }

    return render(request, template, context)


def print_info(request, prints_id):
    """ Print information view """

    prints = get_object_or_404(Prints, pk=prints_id)
    category = Category.objects.all()

    template = 'shop/print_info.html'
    context = {
        'prints': prints,
        'category': category,
    }

    return render(request, template, context)


# Shop admin views
@login_required
def shop_admin(request):
    """ Shop view """

    template = 'shop/shop_admin.html'
    context = {

    }

    return render(request, template, context)


@login_required
def add_print(request):
    """ Add print view """
    category = Category.objects.all()
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES)
        if form.is_valid():
            Prints = form.save()
            messages.success(request, f'Added {prints.name} to {prints.category}.')
            return redirect(reverse('add_print'))
    else:
        form = PrintsForm()
        messages.error(request, f'Please make sure form is valid.')

    template = 'shop/add_print.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def edit_print(request, prints_id):
    category = Category.objects.all()
    prints = get_object_or_404(Prints, pk=prints_id)
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES, instance=prints)
        if form.is_valid():
            form.save()
            messages.success(request, f'Edited {prints.name} in {prints.category}.')
            return redirect(reverse('all_prints'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = PrintsForm(instance=prints)
    messages.info(request, f'Editing {prints.name} in {prints.category}.')

    template = 'shop/edit_print.html'
    context = {
        'form': form,
        'prints': prints,
        'category': category,
    }

    return render (request, template, context)


@login_required
def delete_print(request, prints_id):
    """ Delete print view """
    prints = get_object_or_404(Prints, pk=prints_id)
    prints.delete()
    messages.success(request, f'Deleted {prints.name} from {prints.category}.')
    return redirect(reverse('all_prints'))
