import json
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from shop.views import *
from shop.forms import PriceSelectionForm
from shop.models import Prints


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, prints_id):
    prints = get_object_or_404(Prints, pk=prints_id)
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
                messages.success(request, f'Updated size {size.upper()} {prints.friendly_name} quantity to {bag[prints_id]["prints_by_size"][size]}.')
            else:
                bag[prints_id]['prints_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {prints.friendly_name} to your bag.')
        else:
            bag[prints_id] = {'prints_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {prints.friendly_name} to your bag')
    else:
        if prints_id in list(bag.keys()):
            bag[prints_id] += quantity
            messages.success(request, f'Updated {prints.friendly_name} quantity to {bag[prints_id]}')
        else:
            bag[prints_id] = quantity
            messages.success(request, f'Added {prints.friendly_name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, prints_id):
    prints = get_object_or_404(Prints, pk=prints_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[prints_id]['prints_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {prints.friendly_name} quantity to {bag[prints_id]["prints_by_size"][size]}')
        else:
            del bag[prints_id]['prints_by_size'][size]
            if not bag[prints_id]['prints_by_size']:
                bag.pop(prints_id)
            messages.success(request, f'Removed size {size.upper()} {prints.friendly_name} from your bag')
    else:
        if quantity > 0:        
            bag[prints_id] = quantity
            messages.success(request, f'Updated {prints.friendly_name} quantity to {bag[quantity]}')
        else:
            bag.pop(prints_id)
            messages.success(request, f'Removed {prints.friendly_name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, prints_id):
    try:
        prints = get_object_or_404(Prints, pk=prints_id)
        size = None
        if 'selected_size' in request.POST:
            size = request.POST['selected_size']
        bag = request.session.get('bag', {})

        if size:
                del bag[prints_id]['prints_by_size'][size]
                if not bag[prints_id]['prints_by_size']:
                    bag.pop(prints_id)
                messages.success(request, f'Removed size {size.upper()} {prints.friendly_name} from your bag')
        else:
            bag.pop(prints_id)
            messages.success(request, f'Removed {prints.friendly_name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
