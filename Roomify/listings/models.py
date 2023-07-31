from django.db import models
from django.dispatch import receiver
import logging

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,default=str(id))
    address = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    owner = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=str(id))
    slug = models.CharField(max_length=100,null=True,blank=True,default=str(id))
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(default=0)
    capacity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
@receiver(models.signals.post_save, sender=Room)
def room_saved(sender, instance, created, **kwargs):
    if created:
        logging.info(instance.name + " in " + instance.listing.name + " created")
    else:
        logging.info(instance.name + " in " + instance.listing.name + " updated")
