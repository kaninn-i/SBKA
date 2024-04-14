from django.http import HttpResponse
from django.shortcuts import render, redirect

from booking.forms import AddBookingForm
from booking.models import Booking, Rooms


# Create your views here.


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'booking/index.html', context=data)


def date(request, date_slug):
    db_entry = Booking.objects.filter(date=date_slug).order_by('start_time')

    first_floor_rooms = ['Осень', 'Лето', 'Зима', 'Весна', 'Большой зал', 'Полосатая', 'Каминная', 'Кабинет']
    second_floor_rooms = ['Мансардная', 'Бирюзовая', 'Бордовая']  # лист ожидания как комната??

    # rooms = Rooms.objects.all() - для будущих динамичных комнат

    data = {
        'db_entry': db_entry,
        'date': db_entry[0].date,
        'first_floor_rooms': first_floor_rooms,
        'second_floor_rooms': second_floor_rooms,
    }
    return render(request, 'booking/date.html', context=data)


def add_booking(request):
    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Booking.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, 'Ошибка добавления записи')
    #            добавить куда-то суда ретерн на главную? или не делать? или попробовать сделать ретерн на страницу с этой записью?
    else:
        form = AddBookingForm()

    form = AddBookingForm()
    data = {
        'title': 'Добавление бронирования',
        'form': form
    }

    return render(request, 'booking/add_booking.html', context=data)
