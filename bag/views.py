import json
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.views import *
from shop.forms import PriceSelectionForm
from shop.models import Prints


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, prints_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    
    bag = request.session.get('bag', {})

    if size:
        if prints_id in list(bag.keys()):
            if size in bag[prints_id]['prints_by_size'].keys():
                bag[prints_id]['prints_by_size'][size] += quantity
            else:
                bag[prints_id]['prints_by_size'][size] = quantity
        else:
            bag[prints_id] = {'prints_by_size': {size: quantity}}
    else:
        if prints_id in list(bag.keys()):
            bag[prints_id] += quantity
        else:
            bag[prints_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
