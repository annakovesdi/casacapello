from django.shortcuts import render
from .models import Category, Wines


# return wines
def wines(request):
    wines = Wines.objects.all()
    category = Category.objects.all()
    context = {
        'wines': wines,
        'category': category,
    }
    return render(request, "wines/wines.html", context)
