from django import forms
from .models import Reservation
from .models import BannerImage
from bootstrap_datepicker_plus.widgets import TimePickerInput

import datetime


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['reserved_time', 'date', 'time']

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = '__all__'
