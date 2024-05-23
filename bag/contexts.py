from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from shop.models import Prints

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for prints_id, print_data in bag.items():
        if isinstance(print_data, int):
            selected_print = get_object_or_404(Prints, pk=prints_id)
            
            # total += print_data * 
            product_count += print_data
            bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'selected_print': selected_print,

            })
        else:
            selected_print = get_object_or_404(Prints, pk=prints_id)
            for a4_price, a5_price, quantity in print_data['items_by_size'].items():
                # total += quantity * 
                product_count += quantity
                bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'selected_print': selected_print,
            })

    if total == 0|total > settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0 
        free_delivery_delta = 0
    else:
        delivery = Decimal(settings.DELIVERY_FEE)
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
        }

    return context