from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.shop_admin, name='shop_admin'),
    path('prints/', views.all_prints, name='all_prints'),
    path('<int:prints_id>/', views.print_info, name='print_info'),
    path('add_print/', views.add_print, name='add_print'),
    path('edit_print/<int:prints_id>/', views.edit_print, name='edit_print'),
    path('delete_print/<int:prints_id>/', views.delete_print, name='delete_print'),
    path('add_size', views.add_size, name='add_size')
]
