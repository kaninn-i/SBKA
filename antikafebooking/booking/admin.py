from django.contrib import admin
from .models import Booking, Tags, Rooms


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'room', 'start_time', 'end_time')
    ordering = ['-date', 'start_time', 'room']
    list_per_page = 25
    list_filter = ['date', 'room']
    filter_horizontal = ['tags']


# admin.site.register(Booking, BookingAdmin)

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_per_page = 25


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_per_page = 25