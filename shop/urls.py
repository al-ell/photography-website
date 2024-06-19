from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_admin, name='shop_admin'),
    path('prints/', views.all_prints, name='all_prints'),
    path('<int:prints_id>/', views.print_info, name='print_info'),
    path('add_print/', views.add_print, name='add_print'),
    path('edit_print/<int:prints_id>/', views.edit_print, name='edit_print'),
    path('delete_print/<int:prints_id>/', views.delete_print,
         name='delete_print'),
    path('add_size', views.add_size, name='add_size'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category,
         name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category,
         name='delete_category'),
]
