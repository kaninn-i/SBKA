from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'room', 'start_time', 'end_time')
    ordering = ['-date', 'start_time', 'room']
    list_per_page = 25
    list_filter = ['date', 'room']
    filter_horizontal = ['tags']
# admin.site.register(Booking, BookingAdmin)
