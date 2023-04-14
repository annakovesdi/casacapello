from django import forms
from .models import Wines


class WinesForm(forms.ModelForm):
    class Meta:
        model = Wines
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)
        