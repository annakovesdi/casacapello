from django import forms
from .models import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)
        