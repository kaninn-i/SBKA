from django import forms
from .models import Rooms, Tags, Booking


class AddBookingForm(forms.ModelForm):
    # date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'type': 'date'}))
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), label='Комната', empty_label='Комната не выбрана')
    # name = forms.CharField(max_length=50, label="Имя")
    # phone_number = forms.CharField(max_length=15, label='Номер телефона')
    # how_many_visitors = forms.IntegerField(label='Количество посетителей')
    # start_time = forms.TimeField(label='Начало бронирования', widget=forms.TimeInput(attrs={'type': 'time'}))
    # end_time = forms.TimeField(label='Конец бронирования', widget=forms.TimeInput(attrs={'type': 'time'}))
    # tags = forms.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Тэги')

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }