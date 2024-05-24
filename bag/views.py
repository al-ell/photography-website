import json
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.views import *


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, prints_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if prints_id in list(bag.keys()):
        bag[prints_id] += quantity
    else:
        bag[prints_id] = quantity

    # if request.session == 'POST':
    #     price_size_choice = request.POST.get('price_radio')
        
    #     if price_size_choice:
    #         if prints_id in list(bag.keys()):
    #             if size_choice in bag[prints_id]['items_by_size'].values():
    #                 bag[prints_id]['items_by_size'][price_size_choice] += quantity
    #             else:
    #                 bag[prints_id]['items_by_size'][price_size_choice] = quantity
    #         else:
    #             bag[prints_id] = {'items_by_size': {price_size_choice: quantity}}
    #     else:
    #         messages.error(request, f'Please select a size to add to bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
