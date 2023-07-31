from django.contrib import admin

from .models import (
    Listing,
    Room,
)
# adding more search and other things here:
class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address')
    search_fields = ('name', 'owner', 'address')
    list_filter = ('owner',)
    ordering = ('name',)
    filter_horizontal = ()
    fieldsets = ()

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'listing', 'price', 'capacity')
    search_fields = ('name', 'listing', 'price', 'capacity')
    list_filter = ('listing',)
    ordering = ('name',)
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Listing, ListingAdmin)
admin.site.register(Room, RoomAdmin)