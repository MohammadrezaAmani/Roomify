from rest_framework.serializers import ModelSerializer
from .models import Listing
from .models import Room

class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'name', 'slug', 'address', 'description', 'owner']
    
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'listing', 'name', 'slug', 'description', 'price']