from django.http import HttpResponse


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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle Stripe's payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)