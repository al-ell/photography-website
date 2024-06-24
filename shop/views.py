from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q

from .models import Prints, Category
from .forms import PrintsForm, CategoryForm, PriceSelectionForm


def all_prints(request):
    """ Shop view """
    # begin below variables as none and update as the user filters and sorts
    prints = Prints.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'friendly_name':
                sortkey = 'lower_friendly_name'
                prints = prints.annotate(lower_friendly_name=Lower('friendly_name'))
            elif sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            prints = prints.order_by(sortkey)
        # extra "name__" due to use of foreign keys
        if 'category' in request.GET:
            categories = [request.GET['category']]
            prints = prints.filter(category__name__name__in=categories)
            categories = Category.objects.filter(name__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                                request,
                                "You didn't enter search criteria, please try again.")
                return redirect(reverse('all_prints'))

            queries = Q(friendly_name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
            prints = prints.filter(queries).all()

    current_sorting = f'{sort}_{direction}'

    template = 'shop/prints.html'
    context = {
        'prints': prints,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def print_info(request, prints_id):
    """ Print information view """
    prints = get_object_or_404(Prints, pk=prints_id)
    categories = Category.objects.all()
    template = 'shop/print_info.html'
    context = {
        'prints': prints,
    }

    return render(request, template, context)


# Only logged in superusers can access the views below
# Shop admin views
@login_required
def shop_admin(request):
    """ Manage shop view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))

    prints = Prints.objects.all()
    categories = Category.objects.all()

    if request.GET:
        categories = None
        if 'category' in request.GET:
            categories = [request.GET['category']]
            # Extra use of "name__" due to foreign keys
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # Use of size selection to also filter price
    if request.method == 'POST':
        form = PriceSelectionForm(request.POST, request.FILES)
        if form.is_valid():
            # check if form is valid, then save
            sizes = form.save()
            messages.success(request, f'Added {sizes.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, 'Please make sure form is valid.')
    else:
        form = PriceSelectionForm()

    template = 'shop/add_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_print(request):
    """ Add print view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))

    category = get_object_or_404(Prints, pk=category_id)
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES)
        if form.is_valid():
            # check if form is valid, then save
            prints = form.save()
            messages.success(
                             request,
                             f'Added {prints.name} to {prints.category}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, 'Please make sure form is valid.')
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which category to edit to preload into form
    prints = get_object_or_404(Prints, pk=prints_id)
    category = prints.category.name
    if request.method == 'POST':
        form = PrintsForm(request.POST, request.FILES, instance=prints)
        if form.is_valid():
            # check if form is valid, then save
            form.save()
            messages.success(
                             request,
                             f'Edited {prints.name} in {prints.category}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, 'Please make sure form is valid.')
    else:
        form = PrintsForm(instance=prints)
    messages.info(request, f'Editing {prints.name} in {prints.category}.')

    template = 'shop/edit_print.html'
    context = {
        'form': form,
        'prints': prints,
    }

    return render(request, template, context)


@login_required
def delete_print(request, prints_id):
    """ Delete print view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which print to delete, send user
    # to confirmation page to confirm action
    prints = get_object_or_404(Prints, pk=prints_id)
    if request.method == 'POST':
        prints.delete()
        return redirect('shop_admin')
        messages.success(
                         request,
                         f'Deleted {prints.name} from {prints.category}.')
    return render(request, 'projects/delete_print.html')


@login_required
def add_category(request):
    """ Add category view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            # check if form is valid, then save
            category = form.save()
            messages.success(request, f'Added {category.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, 'Please make sure form is valid.')
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which category to edit to preload into form
    category = get_object_or_404(Prints, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            # check if form is valid, then save
            form.save()
            messages.success(request, f'Edited {category.name}.')
            return redirect(reverse('shop_admin'))
        else:
            messages.error(request, 'Please make sure form is valid.')
    else:
        form = CategoryForm(instance=category)
    messages.info(request, f'Editing {category.name}.')

    template = 'shop/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete category view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin has access to this page.')
        return redirect(reverse('home'))
    # identify which category to delete, send user
    # to confirmation page to confirm action
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('shop_admin')
        messages.success(request, f'Deleted {category.name}.')

    return render(request, 'projects/delete_category.html')
