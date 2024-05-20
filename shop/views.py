from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Category, Print
from projects.models import Project
from .forms import PrintForm


def all_prints(request):
    """ Shop view """

    prints = Print.objects.all()
    category = Category.objects.all()


    template = 'shop/prints.html'
    context = {
        'prints': prints,
        'category': category,
    }

    return render(request, template, context)

# Shop admin views

def shop_admin(request):
    """ Shop view """

    template = 'shop/shop_admin.html'
    context = {

    }

    return render(request, template, context)



def add_print(request):
    """ Add print view """
    category = Category.objects.all()
    if request.method == 'POST':
        form = PrintForm(request.POST, request.FILES)
        if form.is_valid():
            print = form.save()
            # add success msg
            return redirect(reverse('add_print'))
    else:
        form = PrintForm()

    template = 'shop/add_print.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


