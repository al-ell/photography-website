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


    if total == 0 | total > settings.FREE_DELIVERY_THRESHOLD:
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