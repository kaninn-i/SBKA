from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'room', 'start_time', 'end_time')
    ordering = ['-date', 'start_time', 'room']
    list_per_page = 25
# admin.site.register(Booking, BookingAdmin)
