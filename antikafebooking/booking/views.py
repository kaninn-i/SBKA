from django.http import HttpResponse
from django.shortcuts import render, redirect

from booking.forms import AddBookingForm
from booking.models import Booking, Rooms


# Create your views here.


def index(request):

    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddBookingForm()

    data = {
        'title': 'Главная страница',
        'form': form
        }

    return render(request, 'booking/index.html', context=data)


def date(request, date_slug):

    db_entry = Booking.objects.filter(date=date_slug).order_by('start_time')
    rooms = Rooms.objects.all()
    floors = []

    for room in rooms:
        if room.floor not in floors:
            floors.append(room.floor)
        else:
            pass

    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/.')
    else:
        form = AddBookingForm()


    if db_entry:
        data = {
            'db_entry': db_entry,
            'date': db_entry[0].date,
            'rooms': rooms,
            'floors': floors,
            'form': form,
        }
        return render(request, 'booking/date.html', context=data)
    else:
        return HttpResponse('Бронирований на данную дату нет')


def add_booking(request):
    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBookingForm()

    data = {
        'title': 'Добавление бронирования',
        'form': form
    }

    return render(request, 'booking/add_booking.html', context=data)
