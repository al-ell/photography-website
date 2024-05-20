from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Print




def all_prints(request):
    """ Shop view """

    template = 'projects/all_projects.html'
    context = {

    }

    return render(request, template, context)

# Shop admin views

def shop_admin(request):
    """ Shop view """

    template = 'shop/shop_admin.html'
    context = {

    }

    return render(request, template, context)


