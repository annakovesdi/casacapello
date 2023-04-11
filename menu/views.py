from django.shortcuts import render
from .models import Category, Menu


# return menu
def menu(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    context = {
        'menu': menu,
        'category': category,
    }
    return render(request, "menu/menu.html", context)

