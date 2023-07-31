from django.urls import path
from .views import (
    ReservationList,
    ReservationDetail,
)


urlpatterns = [
    path('', ReservationList.as_view()),
    path('<int:pk>/', ReservationDetail.as_view()),
]
