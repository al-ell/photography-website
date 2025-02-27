from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ add lineitem Model to admin section """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ add order admin Model to admin section """
    inlines = (OrderLineItemAdminInline,)
    # prevent change of this information
    readonly_fields = ('date', 'order_number',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('date', 'order_number', 'delivery_cost',
              'order_total', 'grand_total', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county',
              'postcode', 'country', 'original_bag', 'stripe_pid')

    list_display = ('date', 'order_number', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
