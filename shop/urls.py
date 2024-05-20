from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.shop_admin, name='shop_admin'),
    path('prints/', views.all_prints, name='all_prints'),
    path('add_print/', views.add_print, name='add_print'),
    path('<print_id>/', views.print_info, name='print_info'),
]
