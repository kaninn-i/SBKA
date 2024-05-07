from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from booking.forms import AddBookingForm
from booking.models import Booking, Rooms

import datetime


# Create your views here.


def index(request):
    date_today = datetime.date.today()
    return redirect(f'/dates/{date_today}')


def edit_booking(request, pk):
    if request.method == 'GET':
        if pk == 0:
            form = AddBookingForm()
        else:
            book = Booking.objects.get(pk=pk)

            date_str = book.date.strftime('%Y-%m-%d')
            form = AddBookingForm(instance=book, initial={'date': date_str})

            # form = AddBookingForm(instance=book)
        return render(request, 'booking/edit_booking.html', {'form_ed': form, 'pk': pk})
    else:
        if pk == 0:
            form = AddBookingForm(request.POST)
        else:
            book = Booking.objects.get(pk=pk)
            form = AddBookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            date_redirect = form.cleaned_data['date']
        return redirect(f'/dates/{date_redirect}')


def delete_booking(request, pk):
    book = Booking.objects.get(pk=pk)
    book.delete()
    return redirect(f'/dates/{book.date}')


def date(request, date_slug):

    db_entry = Booking.objects.filter(date=date_slug).order_by('start_time')
    rooms = Rooms.objects.all()
    floors = []

    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/dates/{date_slug}')
    else:
        form = AddBookingForm()


    if db_entry:

        for room in rooms:
            if room.floor not in floors:
                floors.append(room.floor)
            else:
                pass

        data = {
            'db_entry': db_entry,
            'date': db_entry[0].date,
            'rooms': rooms,
            'floors': floors,
            'form': form,
        }
        return render(request, 'booking/date.html', context=data)
    else:

        if request.method == 'POST':
            form = AddBookingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(f'/dates/{date_slug}')
        else:
            form = AddBookingForm()

        data = {
            'date': datetime.datetime.strptime(date_slug, '%Y-%m-%d'),
            'form': form,
        }
        return render(request, 'booking/no_bookings.html', context=data)