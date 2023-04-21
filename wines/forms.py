from django import forms
from .models import Wines, BannerImage


class WinesForm(forms.ModelForm):
    class Meta:
        model = Wines
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = '__all__'
