from django.http import HttpResponse
from django.shortcuts import render

from booking.models import Booking

# Create your views here.

first_floor_rooms = ['Осень', 'Лето', 'Зима', 'Весна', 'Большой зал', 'Полосатая', 'Каминная', 'Кабинет']
second_floor_rooms = ['Мансардная', 'Бирюзовая', 'Бордовая']  # лист ожидания как комната??


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'booking/index.html', context=data)


def date(request, date_slug):
    db_entry = Booking.objects.filter(date=date_slug).order_by('start_time')
    data = {
        'db_entry': db_entry,
        'date': db_entry[0].date,
        'first_floor_rooms': first_floor_rooms,
        'second_floor_rooms': second_floor_rooms,
    }
    return render(request, 'booking/date.html', context=data)


def add_booking(request):
    data = {'title': 'Добавление бронирования'}
    return render(request, 'booking/add_booking.html', context=data)
