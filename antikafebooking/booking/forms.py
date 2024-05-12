from django import forms
from .models import Rooms, Booking


class AddBookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), label='Комната', empty_label='Комната не выбрана')

    def __init__(self, *args, **kwargs):
        super(AddBookingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field.widget, forms.CheckboxSelectMultiple):
                pass
            elif isinstance(visible.field, forms.ModelChoiceField):
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'tags': forms.CheckboxSelectMultiple(attrs={}),
        }
