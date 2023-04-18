from django import forms
from .models import Menu
from .models import Category


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('imagebanner',)

