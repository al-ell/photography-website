from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.shop_admin, name='shop'),
    path('prints/', views.all_prints, name='all_prints'),

    
]
