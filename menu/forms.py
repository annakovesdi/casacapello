from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)
        