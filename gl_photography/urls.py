from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path('shop/', include('shop.urls')),
    path('about/', include('about.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # error handlers
# handler404 = 'gl_photograpy.views.handler404'
# handler500 = 'gl_photograpy.views.handler500'
