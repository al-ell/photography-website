import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from shop.models import Prints
from profiles.models import UserProfile


class Order(models.Model):
    """ Order Model """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    full_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=254, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    street_address1 = models.CharField(max_length=100, null=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    city_or_town = models.CharField(max_length=40, null=False)    
    postcode = models.CharField(max_length=20, null=False, default="")
    county = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    original_bag = models.TextField(null=False, default='')
    stripe_pid = models.CharField(max_length=250, null=False, default='')

    def _make_order_number(self):

        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(
                                                    Sum('lineitem_total')
                                                    )['lineitem_total__sum'] or 0
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
    """ Order Items Model """
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='lineitems')
    prints = models.ForeignKey(Prints, null=True, blank=True, on_delete=models.CASCADE)
    selected_size = models.CharField(max_length=2, null=False, default="a4") # A5, A4
    quantity = models.IntegerField(null=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, editable=False)

    def save(self, *args, **kwargs):
        """ Depending on selected size, calculate correct price """
        if self.selected_size == 'a4':
            self.lineitem_total = self.prints.a4_price * self.quantity
        else:
            self.lineitem_total = self.prints.a5_price * self.quantity
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.prints.sku} on order {self.order.order_number}'
