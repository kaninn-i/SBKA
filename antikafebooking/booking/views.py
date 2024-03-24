from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'booking/index.html', context=data)


def date(request, date_id):
    test = {
        'name': 'Илья',
        'phone': '0123456789',
        'visitors': 5,
        'start_time': "10:00",
        'end_time': "15:00",
        'date': date_id
        #    добавить теги (отложено до бд)
    }

    return render(request, 'booking/date.html', context=test)
