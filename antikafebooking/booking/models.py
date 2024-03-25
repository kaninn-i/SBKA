from django.db import models


# Create your models here.

class Booking(models.Model):
    date = models.DateField(db_index=True)
    room = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    how_many_visitors = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
#     добавить теги (булевые) (отдельной таблицей?)


