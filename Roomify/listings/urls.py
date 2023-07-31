from django.urls import path

from .views import (
    ListingList,
    RoomList,
    ListingDetail,
    RoomDetail,
    RoomFilter,
)

app_name = 'listings'

urlpatterns = [
    path('', ListingList.as_view(), name='listings'),
    path('<int:pk>/', ListingDetail.as_view(), name='listing'),
    path('rooms/', RoomList.as_view()),
    path('rooms/<int:pk>/', RoomDetail.as_view()),
    path('rooms/filter/', RoomFilter),
]