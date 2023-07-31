from django.urls import path
from .views import (
    ReservationList,
    ReservationDetail,
    ReservationFilter,
)


urlpatterns = [
    path('', ReservationList.as_view()),
    path('<int:pk>/', ReservationDetail.as_view()),
    path('filter/', ReservationFilter),
]
