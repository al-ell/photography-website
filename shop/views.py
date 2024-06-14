from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Prints, Category
from .forms import PrintsForm, CategoryForm


def all_prints(request):
    """ Shop view """
    prints = Prints.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = [request.GET['category']]
            prints = prints.filter(category__name__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter search criteria, please try agin.")
                return redirect(reverse('all_prints'))
            
            queries = Q(friendly_name__icontains=query) | Q(description__icontains=query) | Q(category__name__name__icontains=query)
            prints = prints.filter(queries).all()

    template = 'shop/prints.html'
    context = {
        'prints': prints,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, template, context)


def print_info(request, prints_id):
    """ Print information view """
    prints = get_object_or_404(Prints, pk=prints_id)
    template = 'shop/print_info.html'
    context = {
        'prints': prints,
    }

    return render(request, template, context)


# Shop admin views
@login_required
def shop_admin(request):
    """ Shop view """
    prints = Prints.objects.all()
    categories = Category.objects.all()

    
    if request.GET:
        categories = None
        if 'category' in request.GET:
            categories = [request.GET['category']]
            prints = prints.filter(category__name__name__in=categories)
            categories = Category.objects.filter(name__name__in=categories)

    template = 'shop/shop_admin.html'
    context = {
        'prints': prints,
        'categories': categories,
    }

    return render(request, template, context)


@login_required
def add_size(request):
    """ Add size and price view """
    
    if request.method == 'POST':
        form = PriceAndSizeForm(request.POST, request.FILES)
        if form.is_valid():
            sizes = form.save()
            messages.success(request, f'Added {sizes.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = PriceAndSizeForm()

    template = 'shop/add_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_print(request):
    """ Add print view """
    category = get_object_or_404(Category)
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES)
        if form.is_valid():
            prints = form.save()
            messages.success(request, f'Added {prints.name} to {prints.category}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = PrintsForm()

    template = 'shop/add_print.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def edit_print(request, prints_id):
    """ Edit print view """
    prints = get_object_or_404(Prints, pk=prints_id)
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES, instance=prints)
        if form.is_valid():
            form.save()
            messages.success(request, f'Edited {prints.name} in {prints.category}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = PrintsForm(instance=prints)
    messages.info(request, f'Editing {prints.name} in {prints.category}.')

    template = 'shop/edit_print.html'
    context = {
        'form': form,
        'prints': prints,
    }

    return render (request, template, context)


@login_required
def delete_print(request, prints_id):
    """ Delete print view """
    prints = get_object_or_404(Prints, pk=prints_id)
    prints.delete()
    messages.success(request, f'Deleted {prints.name} from {prints.category}.')
    return redirect(reverse('shop_admin'))


@login_required
def add_category(request):
    """ Add category view """
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Added {category.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = CategoryForm()

    template = 'shop/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit category view """
    category = get_object_or_404(Prints, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Edited {category.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, f'Please make sure form is valid.')
    else:
        form = CategoryForm(instance=category)
    messages.info(request, f'Editing {category.name}.')

    template = 'shop/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render (request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete category view """
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, f'Deleted {category.name}.')
    return redirect(reverse('shop_admin'))