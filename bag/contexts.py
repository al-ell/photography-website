from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Prints, PriceAndSize

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for prints_id, print_data in bag.items():
        if isinstance(print_data, int):
            selected_print = get_object_or_404(Prints, pk=prints_id)
            # selected_price = 
            # total += print_data * selected_price.price
            product_count += print_data
            bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'selected_print': selected_print,
            })
        else:
            selected_print = get_object_or_404(Prints, pk=prints_id)
            for size, quantity in print_data['items_by_size'].items():
                # total += quantity * price
                product_count += quantity
                bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'selected_print': selected_print,
                'size': size,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.DELIVERY_FEE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else: 
        delivery = 0 
        free_delivery_delta = 0
    
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