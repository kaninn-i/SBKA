from django.db import models
from wheel.vendored.packaging.tags import Tag


# Create your models here.

class Booking(models.Model):
    ROOMS_CHOICES = [
        ('Кабинет', 'Кабинет'),
        ('Каминная', 'Каминная'),
        ('Большой зал', 'Большой зал'),
        ('Полосатая', 'Полосатая'),
        ('Лето', 'Лето'),
        ('Осень', 'Осень'),
        ('Зима', 'Зима'),
        ('Весна', 'Весна'),
        ('Бордовая', 'Бордовая'),
        ('Мансардная', 'Мансардная'),
        ('Бирюзовая', 'Бирюзовая')
        # добавить сюда лист ожидания в виде комнаты?
    ]

    date = models.DateField(db_index=True, verbose_name='Дата')
    room = models.ForeignKey('Rooms', on_delete=models.DO_NOTHING, verbose_name='Комната')
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone_number = models.CharField(max_length=15)
    how_many_visitors = models.IntegerField()
    start_time = models.TimeField(verbose_name='Начало бронирования')
    end_time = models.TimeField(verbose_name='Конец бронирования')
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Тэги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись о бронировании'
        verbose_name_plural = 'Записи о бронировании'


class Tags(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name='Тэг')
    meaning = models.CharField(max_length=255, db_index=True, verbose_name='Значение', blank=True, null=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Rooms(models.Model):
    room_name = models.CharField(max_length=100, db_index=True, verbose_name='Название комнаты')
    description = models.CharField(max_length=255, db_index=True, verbose_name='Описание комнаты')

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
