import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from shop.models import Prints


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    full_name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    city_or_town = models.CharField(max_length=40, null=False, blank=False)    
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)

    def _make_order_number(self):

        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.DELIVERY_FEE
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save( )
    
    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._make_order_number()
        super().save(*args, **kwargs)
   

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    prints = models.ForeignKey(Prints, null=False, blank=False, on_delete=models.CASCADE)
    prints_size = models.CharField(max_length=2, null=True, blank=True) # A5, A4
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        
        """
        
        self.lineitem_total = self.prints.a4_price * self.quantity
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.prints.sku} on order {self.order.order_number}'
