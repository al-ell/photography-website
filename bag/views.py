from django.shortcuts import render, redirect
from shop.models import PriceAndSize
from shop.views import *


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, prints_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'price_radio' in request.POST:
        size = request.POST['price_radio']

    bag = request.session.get('bag', {})

    if size:
        if prints_id in list(bag.keys()):
            if size in bag[prints_id]['items_by_size'].keys():
                bag[prints_id]['items_by_size'][size] += quantity
            else:
                bag[prints_id]['items_by_size'][size] = quantity
        else:
            bag[prints_id] = {'items_by_size': {size: quantity}}
    else:
        messages.error(f'Please select a size to add to bag')


    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
