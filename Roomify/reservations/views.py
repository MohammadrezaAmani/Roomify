from .models import (
    Reservation,
)

from .serializers import (
    ReservationSerializer,
)
from .funcs import (
    is_free,
)

from rest_framework import  generics
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def perform_create(self, serializer):
        if is_free(serializer.validated_data):
            serializer.save()
        else:
            raise Http404

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
# check availibility using pk and dates
@api_view(['GET'])
def ReservationFilter(request):
    room = request.query_params.get('room', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    if room is not None and start_date is not None and end_date is not None:
        if is_free({'room': room, 'start_date': start_date, 'end_date': end_date}):
            return Response({'is_free': True})
        return Response({'is_free': False})
    if room is not None and start_date is None and end_date is None:
        queryset = Reservation.objects.filter(room=room)
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)