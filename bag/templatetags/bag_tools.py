from django import template
from shop.models import Prints


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(quantity):
    prints = get_object_or_404(Prints, pk=prints_id)
    if size == 'a4':
        return prints.a4_price * quantity
    else:
        return prints.a5_price * quantity
