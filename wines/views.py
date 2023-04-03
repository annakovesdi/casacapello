from django.shortcuts import render
from .models import Wines


# return wines
def wines(request):
    wines = Wines.objects.all()
    category = Category.objects.all()
    context = {
        'wines': wines,
        'category': category,
    }
    return render(request, "w/wijnkaart.html", context)