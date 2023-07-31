from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls'), name='listings'),
    path('reservations/', include('reservations.urls'), name='reservations'),
]
