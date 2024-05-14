from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from booking.forms import AddBookingForm
from booking.models import Booking, Rooms

import datetime


# Create your views here.


def index(request):
    # переадресация пользователя с главной страницы
    # на страницу текущей даты
    date_today = datetime.date.today()
    return redirect(f'/dates/{date_today}')


def edit_booking(request, pk):
    if request.method == 'GET':
        # получение данных о формах и их передача в html-документ
        form = AddBookingForm()
        if pk == 0:
            form_ed = AddBookingForm()
        else:
            book = Booking.objects.get(pk=pk)
            date_str = book.date.strftime('%Y-%m-%d')
            form_ed = AddBookingForm(instance=book, initial={'date': date_str})
        return render(request, 'booking/edit_booking.html', {'form_ed': form_ed, 'pk': pk, 'form': form})

    elif request.method == 'POST':
        # обработка полученных данных форм,
        # добавление или изменение записи в БД в зависимости от заполненной формы
        if 'edit_form_submit' in request.POST:
            form_ed = AddBookingForm(request.POST)
            if form_ed.is_valid():
                if pk == 0:
                    form_ed.save()
                else:
                    book = Booking.objects.get(pk=pk)
                    form_ed = AddBookingForm(request.POST, instance=book)
                    form_ed.save()
                    date_redirect = form_ed.cleaned_data['date']
                    return redirect(f'/dates/{date_redirect}')
        elif 'save_form_submit' in request.POST:
            form = AddBookingForm(request.POST)
            if form.is_valid():
                form.save()
            date_redirect = form.cleaned_data['date']
            return redirect(f'/dates/{date_redirect}')
        # return redirect('/')


def delete_booking(request, pk):
    # получение необходимого обьекта из базы данных и его удаление
    book = Booking.objects.get(pk=pk)
    book.delete()
    return redirect(f'/dates/{book.date}')


def date(request, date_slug):
    # получение информации из базы данных
    db_entry = Booking.objects.filter(date=date_slug).order_by('start_time')
    rooms = Rooms.objects.all()
    floors = []

    # отображение и обработка формы для добавления бронирований
    if request.method == 'POST':
        form = AddBookingForm(request.POST)
        if form.is_valid():
            form.save()
            date_redirect = form.cleaned_data['date']
            return redirect(f'/dates/{date_redirect}')
    else:
        form = AddBookingForm()

    # в зависимости от наличия бронирований на дату отрисовка нужного Html-документа
    # + передача в него необходимых данных
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
        data = {
            'date': datetime.datetime.strptime(date_slug, '%Y-%m-%d'),
            'form': form,
        }
        return render(request, 'booking/no_bookings.html', context=data)
