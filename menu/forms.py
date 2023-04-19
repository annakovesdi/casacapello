from django import forms
from .models import Menu
from .models import BannerImage


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = '__all__'
