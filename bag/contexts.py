from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Prints
from shop.forms import PriceSelectionForm


def bag_contents(request):
    """ Bag contents view """
    # begin variables at zero and build as the customer adds to their bag
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    bag = request.session.get('bag', {})
    # Get the correct price for the selected size in the form
    form = PriceSelectionForm(request.POST)

    # Create data for bag items from selected prints info with or without size
    for prints_id, print_data in bag.items():
        if isinstance(print_data, int):
            prints = get_object_or_404(Prints, pk=prints_id)
            total += print_data * prints.a4_price
            product_count += print_data
            bag_items.append({
                'prints_id': prints_id,
                'quantity': print_data,
                'prints': prints,
                'form': form,
            })
        else:
            prints = get_object_or_404(Prints, pk=prints_id)
            for size, quantity in print_data['prints_by_size'].items():
                # if a4 size is seleced:
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
                    # if a5 size is selected
                    total += quantity * prints.a5_price
                    product_count += quantity
                    bag_items.append({
                        'prints_id': prints_id,
                        'quantity': quantity,
                        'prints': prints,
                        'size': size,
                        'form': form,
                    })

    # Calculate delivery based on customer spend
    if total > settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0
        free_delivery_delta = 0
    elif total == 0:
        delivery = 0
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD
    else:
        delivery = 4
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    grand_total = delivery + total
    # create and return context
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
