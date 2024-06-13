from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from shop.models import Prints
from shop.forms import PriceSelectionForm

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    form = PriceSelectionForm(request.POST)

    for prints_id, print_data in bag.items():
        if isinstance(print_data, int):
            prints = get_object_or_404(Prints, pk=prints_id)
            total += print_data * prints.a4_price
            product_count =+ print_data
            bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'prints': prints,
                'form': form, 
            })
        else:
            prints = get_object_or_404(Prints, pk=prints_id)
            for size, quantity in print_data['prints_by_size'].items():
                if size == 'a4':
                    total += quantity * prints.a4_price
                    product_count += quantity
                    bag_items.append({
                    'prints_id': prints_id,
                    'quantity': quantity,
                    'prints': prints,
                    'form': form, 
                    'size': size,
                    })
                else:
                    total += quantity * prints.a5_price
                    product_count += quantity
                    bag_items.append({
                    'prints_id': prints_id,
                    'quantity': quantity,
                    'prints': prints,
                    'size': size,
                    'form': form, 
                    })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0 
        free_delivery_delta = 0
    else:
        delivery = settings.DELIVERY_FEE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'free_delivery_delta': free_delivery_delta, 
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'delivery': delivery,
        'product_count': product_count,
        'form': form,
        }

    return context