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
    
# TODO: check availability
