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

    for prints_id, quantity in bag.items():
        prints = get_object_or_404(Prints, pk=prints_id)
        total += quantity * prints.a4_price
        product_count =+ quantity
        bag_items.append({
            'prints_id': prints_id,
            'quantity': quantity,
            'prints': prints,
            'form': form, 
        })



    if not bag_items and total < settings.FREE_DELIVERY_THRESHOLD:
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
        'form': form,
        }

    return context