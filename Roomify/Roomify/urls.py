from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Reservation API",
        default_version='v1',
        description="API endpoints for my application",
        contact=openapi.Contact(email="contact@myapi.local"),
    ),
    public=True,
)
include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls'), name='listings'),
    path('reservations/', include('reservations.urls'), name='reservations'),
    path('reports/', include('reports.urls'), name='reports'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]