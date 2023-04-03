from django.shortcuts import render
from .models import About
from .forms import AboutForm


# return homepage
def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }
    return render(request, "about/about.html", context)

