from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Listing,
    Room
)
from .serializers import (
    ListingSerializer,
    RoomSerializer
)

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# example = 127.0.0.1:8000/listings/rooms/?listing=1&capacity=2&price=100
@api_view(['GET'])
def RoomFilter(request):
    """http://127.0.0.1:8000/api/v1/listings/rooms/filter/?name=string&price=0
    """
    queryset = Room.objects.all()
    listing = request.query_params.get('listing', None)
    capacity = request.query_params.get('capacity', None)
    price = request.query_params.get('price', None)
    name = request.query_params.get('name', None)
    id = request.query_params.get('id', None)
    if listing is not None:
        queryset = queryset.filter(listing=listing)
    if capacity is not None:
        queryset = queryset.filter(capacity=capacity)
    if price is not None:
        queryset = queryset.filter(price=float(price))
    if name is not None:
        queryset = queryset.filter(name=name)
    if id is not None:
        queryset = queryset.filter(id=int(id))
    serializer = RoomSerializer(queryset, many=True)
    return Response(serializer.data)