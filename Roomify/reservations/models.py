from django.db import models
import logging
from listings.models import Room
from django import dispatch

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=100)
    guest_email = models.CharField(max_length=100)
    guest_phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.guest_name + " at " + self.room.name
    
@dispatch.receiver(models.signals.post_save, sender=Reservation)
def reservation_saved(sender, instance, created, **kwargs):
    if created:
        logging.info(instance.guest_name + " at " + instance.room.name + " in " + instance.room.listing.name + " created")
    else:
        logging.info(instance.guest_name + " at " + instance.room.name + " in " + instance.room.listing.name + " updated")