from django.urls import path
from .views import ReportView

app_name = 'reports'

urlpatterns = [
    path('listings/<int:listing_id>/report/', ReportView.as_view(), name='listing_report'), 
]