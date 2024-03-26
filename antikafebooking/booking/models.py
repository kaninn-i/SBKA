from django.db import models
from wheel.vendored.packaging.tags import Tag


# Create your models here.

class Booking(models.Model):
    date = models.DateField(db_index=True)
    room = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    how_many_visitors = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    tags = models.OneToOneField('Tags', on_delete=models.CASCADE, related_name='booking', null=True, blank=True)


class Tags(models.Model):
    min_booking = models.BooleanField(default=0)
    no_min_booking = models.BooleanField(default=0)
    projector = models.BooleanField(default=0)
    payment_by_organizer = models.BooleanField(default=0)
    mastermind = models.BooleanField(default=0)
    rhetoric = models.BooleanField(default=0)
    poufs = models.BooleanField(default=0)
    flipchart = models.BooleanField(default=0)
    laptop = models.BooleanField(default=0)
    coaching_rate = models.BooleanField(default=0)
    tea_rate = models.BooleanField(default=0)
    coffee_rate = models.BooleanField(default=0)
    birthday = models.BooleanField(default=0)
