from django.http import HttpResponse
from .models import Order, OrderLineItem
from shop.models import Prints
import json
import time


class StripeWH_Handler:
    """Handle Stripe's webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic/unknown/unexpected Stripe webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):
        """
        Handle Stripe's payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1_name__iexact=shipping_details.address.line1,
                    street_address2_name__iexact=shipping_details.address.line2,
                    city_or_town__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1_name=shipping_details.address.line1,
                    street_address2_name=shipping_details.address.line2,
                    city_or_town=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for prints_id, print_data in json.loads(bag).items():
                    prints = Prints.objects.get(id=prints_id)
                    if isinstance(print_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            prints=prints,
                            quantity=print_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in print_data['prints_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                prints=prints,
                                quantity=quantity,
                                prints_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle Stripe's payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
