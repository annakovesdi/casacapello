from django.shortcuts import render
from .models import Home
from .forms import HomeForm


# return homepage
def home(request):
    home = Home.objects.all()
    context = {
        'home': home,
    }
    return render(request, "home/home.html", context)

