from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
