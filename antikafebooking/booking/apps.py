from django.apps import AppConfig


class BookingConfig(AppConfig):
    verbose_name = 'Бронирования'
    verbose_name_plural = 'Бронирования'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
