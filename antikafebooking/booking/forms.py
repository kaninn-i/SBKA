from django import forms
from .models import Rooms, Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class AddBookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), label='Комната', empty_label='Комната не выбрана')

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'tags': forms.CheckboxSelectMultiple(),
        }