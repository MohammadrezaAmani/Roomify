from rest_framework.serializers import ModelSerializer
from .models import Reservation

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'start_date', 'end_date', 'guest_name', 'guest_email', 'guest_phone']