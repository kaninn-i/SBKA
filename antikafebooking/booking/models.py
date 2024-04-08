from django.db import models
from wheel.vendored.packaging.tags import Tag


# Create your models here.

class Booking(models.Model):
    date = models.DateField(db_index=True, verbose_name='Дата')
    room = models.CharField(max_length=50, verbose_name='Комната')
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone_number = models.CharField(max_length=15)
    how_many_visitors = models.IntegerField()
    start_time = models.TimeField(verbose_name='Начало бронирования')
    end_time = models.TimeField(verbose_name='Конец бронирования')
    tags = models.OneToOneField('Tags', on_delete=models.SET_NULL, related_name='book', null=True, blank=True)

    class Meta:
        verbose_name = 'Запись о бронировании'
        verbose_name_plural = 'Записи о бронировании'

class Tags(models.Model):
    min_booking = models.BooleanField(blank=True, default=0)
    no_min_booking = models.BooleanField(blank=True, default=0)
    projector = models.BooleanField(blank=True, default=0)
    payment_by_organizer = models.BooleanField(blank=True, default=0)
    mastermind = models.BooleanField(blank=True, default=0)
    rhetoric = models.BooleanField(blank=True, default=0)
    poufs = models.BooleanField(blank=True, default=0)
    flipchart = models.BooleanField(blank=True, default=0)
    laptop = models.BooleanField(blank=True, default=0)
    coaching_rate = models.BooleanField(blank=True, default=0)
    tea_rate = models.BooleanField(blank=True, default=0)
    coffee_rate = models.BooleanField(blank=True, default=0)
    birthday = models.BooleanField(blank=True, default=0)
