from django.db import models


# Create your models here.

# CharField - текст

class Booking(models.Model):
    date = models.DateField()
    name = models.CharField()
